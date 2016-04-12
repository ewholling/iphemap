from ipscdb.models import Gene, Phenotype
from django.utils.encoding import smart_str
import csv

def export():
  with open('data.csv', 'wb') as f:
    writer = csv.writer(f)
    genes = Gene.objects.all()
    for g in genes:
      for i, p in enumerate(g.phenotypes.all()):
        if i == 0:
          writer.writerow([smart_str(a) for a  in [g.name, g.disease, g.snp, g.pmid, p.domain, p.description]])
        else:
          writer.writerow([smart_str(a) for a  in ['', '', '', '', p.domain, p.description]])


        




