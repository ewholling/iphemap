from bs4 import BeautifulSoup
from models import Gene, Phenotype

def extract_data():
	EXCEL_DATA_START = 'E4'
	EXCEL_DATA_END = 'PX77'
	
	data_start_col = ord(EXCEL_DATA_START[0]) - 65
	data_start_row = int(EXCEL_DATA_START[1]) - 1
	data_end_col = 26*(ord(EXCEL_DATA_END[0]) - 64) + ord(EXCEL_DATA_END[1]) - 64
	data_end_row = int(EXCEL_DATA_END[2:4])
	# load map
	with open('../../../data/map.htm', 'r') as f:
		soup = BeautifulSoup('\n'.join(f.readlines()))
		tb = soup.tbody
	
	# print data_start_row, data_start_col, len(tb.find_all('tr')[2].find_all('td'))
	# print data_end_row, data_end_col
	# return
	
	# get index
	domain_index = {}
	for i in xrange(2):
		for t in tb.find_all('tr')[i].find_all(
				(lambda e: 'bgcolor' in e.attrs and len(e.get_text()) > 0)):
			domain_index[t['bgcolor']] = t.get_text()

		print '%s %s' % (t['bgcolor'],t.get_text())

	# get pulications
	# for i in xrange(data_start_col, len(tb.find_all('tr')[2].find_all('td'))):
	for i in xrange(data_start_col, data_end_col):
		desc = tb.find_all('tr')[2].find_all('td')[i].get_text()
		if len(p) > 0:
			phenotype = Phenotype(pk = i, description = desc)
			phenotype.save()


	# for i in xrange(data_start_row, len(tb.find_all('tr'))):
	for i in xrange(data_start_row, data_end_row):
		disease 	= tb.find_all('tr')[i].find_all('td')[0].get_text()
		name 		= tb.find_all('tr')[i].find_all('td')[1].get_text()
		mutation	= tb.find_all('tr')[i].find_all('td')[2].get_text()
		
		gene = Gene(name = name, disease = disease, snp = mutation)
		gene.save()

		for j in xrange(data_start_col, data_end_col):
			t = tb.find_all('tr')[i].find_all('td')[j]
			if 'bgcolor' in t.attrs:
				print name, domain_index(t['bgcolor']), p.description
				
				try:
					p = Phenotype.objects.get(pk = j)
					p.domain = domain_index(t['bgcolor'])
					p.save()
					
					gene.phenotypes.add(p)
					gene.save()
				except ObjectDoesNotExist:
					print 'failed to find phenotype by index.'

def extract_figures():
	for l in os.listdir('/home/sachin/Projects/ipscdb/data/molecularphenotypefigures'):
	    k = l.replace('.pdf', '').split()
	    h = None
	    if k[2].startswith('Down') and k[3].startswith('Gene'):     h = 0
	    elif k[2].startswith('Up') and k[3].startswith('Gene'):     h = 1
	    elif k[2].startswith('Down') and k[3].startswith('Path'):   h = 2
	    elif k[2].startswith('Up') and k[3].startswith('Path'):     h = 3
	    else:
	        print k
	        continue
	    print k
	    f = Figure(gene_name = k[0], domain = k[1], hindex=h, pmid = int(k[4]) if len(k) > 4 else -1, filename=l)
	    f.save()
	    