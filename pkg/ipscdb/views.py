from django.shortcuts import render, render_to_response
from django.db.models import Q

from ipscdb.models import Gene, Phenotype, Study, Figure, Announcement

import re
import time

# http://julienphalip.com/post/2825034077/adding-search-to-a-django-site-in-a-snap
def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

# --------------------------------------------- VIEWS -------------------------------------------

def studies(request):
    pmid = request.GET.get('pmid', 0)
    sort_mode = request.GET.get('sort', '')
    studies = Study.objects.all()
    
    if sort_mode:
        try:
            studies = studies.order_by(sort_mode)
        except: pass
    return render_to_response('ipscdb/studies.html', {
        'studies' : studies,
        'selected_pmid' : int(pmid),
        'request' : {'path' : request.path},
        })

def search(request):
    found = None
    query = None
    diseases = sorted(list(set([p.values()[0] 
        for p in Gene.objects.all().values('disease') if p.values()[0]])))
    alldomains = sorted(list(set([p.values()[0] 
        for p in Phenotype.objects.all().values('domain') if p.values()[0]])))
    
    domain_select = request.GET.get('domain-select', '')
    disease_select = request.GET.get('disease-select', '')
    # print domain_select
    # print disease_select
    q = request.GET.get('search', '')
    if len(q) > 0 or disease_select or domain_select:
        domain_select = domain_select if domain_select != 'all' else None
        disease_select = disease_select if disease_select != 'all' else None
        print 'filterng disease: %s' % str(disease_select)
        print 'filterng domain: %s' % str(domain_select)

        if len(q) > 0:
            query = get_query(q, ['name', 'disease', 'snp', 'pmid']) | Q(phenotypes__description__icontains=q)
        
        if disease_select:
            q1 = Q(disease = disease_select)
            query = (query & q1) if query else q1
        
        if query:
            found = Gene.objects.filter(query).prefetch_related('phenotypes')
        else:
            found = Gene.objects.all()

        found = sorted(found, key=lambda x: (x.name, x.pmid))

        # deduplicate
        if len(found) > 0:
            temp = [found[0]]
            for f in found:
                inother = False
                for f1 in temp:
                    if f == f1 or set(f.phenotypes.all()) == set(f1.phenotypes.all()):
                        inother = True
                if not inother:
                    temp.append(f)
            found = temp

        for f in found:
            chosen_phenotypes = f.phenotypes.all().filter(domain__icontains = domain_select) if domain_select else f.phenotypes.all()
            domains = sorted(list(set([p.values()[0] for p in chosen_phenotypes.all().values('domain')])))
            f.sorted_phenotypes = []
            for d in alldomains:
                # figures = Figure.objects.filter(pmid = f.pmid)
                figures = Figure.objects.filter(pmid = f.pmid, domain = d)
                fset = []
                for i in range(4):
                    try:
                        fset.append(figures.get(hindex = i))
                    except:
                        fset.append(None)
                f.sorted_phenotypes.append({
                    'visible'       : d in domains,
                    'name'          : d,
                    'phenotypes'    : chosen_phenotypes.filter(domain = d),
                    # 'figure0'       : fset[0],
                    # 'figure1'       : fset[1],
                    # 'figure2'       : fset[2],
                    # 'figure3'       : fset[3],
                    'figures'       : fset,
                    'showphenotypes': not len(chosen_phenotypes.filter(domain = d)) == 0,
                    'showfigures'   : any([True if fg != None else False for fg in fset]),
                    })
                # print fset, any([True if fg != None else False for fg in fset])
            f.showgenefigures = any([d['showfigures'] for d in f.sorted_phenotypes])
            f.showgenephenotypes = any([d['showphenotypes'] for d in f.sorted_phenotypes])
            # f.showgenephenotypes = True

        return render(request, 'ipscdb/alt.html', {
            'found'     : found,
            'query'     : q,
            'diseases'  : diseases,
            'domains'   : alldomains,
            'request' : {'path' : request.path},
            })
    else:
        return render_to_response('ipscdb/alt.html', {
            'diseases'  : diseases,
            'domains'   : alldomains,
            'request' : {'path' : request.path},
            })

def about(request):
    announcements = Announcement.objects.all()
    return render_to_response('ipscdb/about.html', {'announcements' : announcements, 'request' : {'path' : request.path}})

def faqs(request):
    return render_to_response('ipscdb/faqs.html', {'request' : {'path' : request.path}})

def research(request):
    return render_to_response('ipscdb/research.html', {'request' : {'path' : request.path}})

def contact(request):
    return render_to_response('ipscdb/contact.html', {'request' : {'path' : request.path}})

def disclaimer(request):
    return render_to_response('ipscdb/disclaimer.html', {'request' : {'path' : request.path}})
