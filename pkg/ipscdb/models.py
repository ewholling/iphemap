from django.db import models
from unidecode import unidecode
# Create your models here.

class Study(models.Model):
  first_author        = models.CharField(max_length=1000)
  disease             = models.CharField(max_length=1000)
  snp                 = models.CharField(max_length=1000)
  species             = models.CharField(max_length=1000)
  year                = models.IntegerField(default=0)
  reprogramming_type  = models.CharField(max_length=1000)
  starting_cell_type  = models.CharField(max_length=1000)
  target_cell_type    = models.CharField(max_length=1000)
  disease_patients    = models.CharField(max_length=1000)
  control_patients    = models.CharField(max_length=1000)
  utilization         = models.BooleanField(default=False)
  geoid               = models.CharField(max_length=1000, default='')
  platform_name       = models.CharField(max_length=1000, default='')
  platform_geo_id     = models.CharField(max_length=1000, default='')
  pmid                = models.IntegerField(default=0)
  
  def __str__(self):
    return str(self.pmid)
  class Meta:
    ordering          = ('year',)

class Phenotype(models.Model):
  description         = models.CharField(max_length=1000)
  domain              = models.CharField(max_length=200)

  def __str__(self):
    return unidecode(self.description)
  class Meta:
    ordering          = ('description',)

class Gene(models.Model):
  name                = models.CharField(max_length=200)
  disease             = models.CharField(max_length=200)
  snp                 = models.CharField(max_length=200)
  pmid                = models.IntegerField(default=0)
  phenotypes          = models.ManyToManyField(Phenotype)

  def __str__(self):
    return self.name
  class Meta:
    ordering          = ('name', 'pmid')

class Figure(models.Model):
  gene_name           = models.CharField(max_length=200)
  domain              = models.CharField(max_length=200)
  hindex              = models.IntegerField(default=0)
  pmid                = models.IntegerField(default=0)
  filename            = models.CharField(max_length=200)

  def __str__(self):
    return '<{0} {1} : {2} : {3}>'.format(self.gene_name, self.domain, self.pmid, self.hindex)
  class Meta:
    ordering          = ('hindex',)

class Announcement(models.Model):
  date                = models.DateField(auto_now_add=True)
  title               = models.CharField(max_length=1000)
  link                = models.CharField(max_length=1000, blank=True)

  def __str__(self):
    return '<{0} : {1} : {2}>'.format(self.date, self.title, self.link)
  class Meta:
    ordering          = ('date',)
