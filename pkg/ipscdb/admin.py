from django.contrib import admin
from ipscdb.models import Gene, Phenotype, Study, Figure, Announcement

admin.site.register(Gene)
admin.site.register(Phenotype)
admin.site.register(Study)
admin.site.register(Figure)
admin.site.register(Announcement)

admin.site.site_header = 'iPhemap Admin Page'
