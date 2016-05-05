from bs4 import BeautifulSoup
from ipscdb.models import Gene, Phenotype, Study, Figure
from django.core.exceptions import ObjectDoesNotExist
import os
import re
import csv

def new_csv(fn):
  with open(fn) as f:
    reader = csv.reader(f)
    hds = next(reader)
    Gene.objects.all().delete()
    Phenotype.objects.all().delete()
    
    gene = None
    for r in reader:
      if r[0] != '':
        if gene:
          # save last gene
          gene.save()
          print(gene, gene.snp)
          print ''
          
        print r
        pmid = int(r[3])
        gene = Gene(name = r[0], disease = r[1], snp = r[2], pmid=pmid)
        gene.save()

        p = Phenotype(description=r[5], domain=r[4])
        p.save()

        gene.phenotypes.add(p)
        print 'added: ', r[5]
      else:
        p = Phenotype(description=r[5], domain=r[4])
        p.save()
        print 'added: ', r[5]
        gene.phenotypes.add(p)

    gene.save()
    print(gene, gene.snp)
          


def extract_figures():
	Figure.objects.all().delete()
	for f in os.listdir('/home/sachin/drive/projects/ipscdb/data/molecularphenotypefigures/'):
		if not f.endswith('pdf'): continue
		p = f.split()
		print p
		hindex = None
		if p[2] == 'Up' and p[3].startswith('Gene'):		hindex = 0
		elif p[2] == 'Down' and p[3].startswith('Gene'):	hindex = 1
		elif p[2] == 'Up' and p[3].startswith('Path'):		hindex = 2
		elif p[2] == 'Down' and p[3].startswith('Path'):	hindex = 3
		else:
			print '\nError 1 {0}'.format(f)
			continue

		try:
			f = Figure(gene_name = p[0], 
				domain=p[1] if p[1].endswith('s') else p[1] + 's', 
				hindex=hindex, 
				pmid=int(p[-1].split('.')[0]),
				filename=f)
			f.save()
		except:
			print 'Error 2 {0}'.format(f)


### OLD
            
def extract_data():
    EXCEL_DATA_START = 'E3'
    EXCEL_DATA_END = 'PT76'
    data_start_col = ord(EXCEL_DATA_START[0]) - 65
    data_start_row = int(EXCEL_DATA_START[1]) - 1
    data_end_col = 26*(ord(EXCEL_DATA_END[0]) - 64) + ord(EXCEL_DATA_END[1]) - 64
    data_end_row = int(EXCEL_DATA_END[2:4])
    # load map
    PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

    # reset Phenotypes, Genes
    Phenotype.objects.all().delete()
    Gene.objects.all().delete()

    with open(PROJECT_PATH + '/../../data/mapnew.html', 'r') as f:
        soup = BeautifulSoup('\n'.join(f.readlines()), 'lxml')
        tb = soup.tbody
    
    # print data_start_row, data_start_col, len(tb.find_all('tr')[2].find_all('td'))
    # print data_end_row, data_end_col
    # return
    
    # get index
    print 'Getting Domain Index'
    domain_index = {}
    # for t in tb.find_all('tr')[0].find_all((lambda e: 'bgcolor' in e.attrs and len(e.get_text()) > 0)):
    for t in tb.find_all('tr')[0].find_all((lambda e: 'style' not in e.attrs and len(e.get_text()) > 0)):
        domain_index[t.attrs['class'][0]] = t.get_text()
        print '%s %s' % (t.attrs['class'][0], t.get_text())
    print domain_index

    # get phenotypes
    # for i in xrange(data_start_col, len(tb.find_all('tr')[2].find_all('td'))):
    print 'Getting Phenotypes'
    h = tb.find_all('tr')[1].find_all('td')
    for i in xrange(data_start_col, data_end_col):
        desc = h[i].get_text()
        if len(desc) > 0:
            try:
                domain = [v for v in domain_index.values() if v[:-1] in desc or v[:-1].lower() in desc][0]
            except:
                if 'neurites' in desc: domain = u'Neurons'
                else: return
            print domain, desc
            phenotype = Phenotype(pk = i, description = desc, domain = domain)
            phenotype.save()
    
    # for i in xrange(data_start_row, len(tb.find_all('tr'))):
    print 'Getting Genes'
    h = tb.find_all('tr')
    for i in xrange(data_start_row, data_end_row):
        g = h[i].find_all('td')
        disease     = g[1].get_text()
        name        = g[2].get_text()
        mutation    = g[3].get_text()
        pmid        = int(re.findall('\d+', g[-1].get_text())[0])
        
        gene = Gene(name = name, disease = disease, snp = mutation, pmid = pmid)
        gene.save()

        for j in xrange(data_start_col, data_end_col):
            t = g[j]
            if t.attrs['class'][0] in domain_index:
                try:
                    p = Phenotype.objects.get(pk = j)
                    # p.domain = domain_index[t.attrs['class'][0]]
                    # if j < 341 and 'Neurons' not in p.domain:
                    #     if 'Neurons' in p.description:
                    #         p.domain = u'Neurons'
                    # p.save()
                    
                    gene.phenotypes.add(p)
                    gene.save()
                    print disease, name, mutation, '\t', p.description
                except ObjectDoesNotExist:
                    print 'failed to find phenotype by index.'
                
def extract_studies_links():
    for s in Study.objects.all():
        f = [g['href'] for g in gses if g.text == s.geoid]
        h = [g['href'] for g in gpls if g.text == s.platform_geo_id]
        if f:
            print f
            s.geoid_link = unidecode(f[0])
        else:
            s.geoid_link = ''
        if h:
            print h
            s.platform_geoid_link = unidecode(h[0])
        else:
            s.platform_geoid_link = ''
        s.save()

def extract_studies(fn):
  Study.objects.all().delete()

  with open(fn) as f:
    reader = csv.reader(f)
    hs = next(reader)

    for l in reader:
      s = Study(
        first_author        = l[1],
        disease             = l[2],
        snp                 = l[3],
        species             = l[4],
        year                = int(l[5]),
        reprogramming_type  = l[6],
        starting_cell_type  = l[7],
        target_cell_type    = l[11],
        disease_patients    = l[8],
        control_patients    = l[9],
        utilization         = True if l[10] == 'Yes' else False,
        geoid               = l[12] if l[12].strip() != '-' else '',
        platform_name       = l[13] if l[13].strip() != '-' else '',
        platform_geo_id     = l[14] if l[14].strip() != '-' else '',
        pmid                = int(re.findall('\d+', l[15])[0]))
      print s 
      s.save()
