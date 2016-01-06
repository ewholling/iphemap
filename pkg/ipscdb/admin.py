from django.contrib import admin
from ipscdb.models import Gene, Phenotype, Study, Figure

admin.site.register(Gene)
admin.site.register(Phenotype)
admin.site.register(Study)
admin.site.register(Figure)
# Register your models here.
