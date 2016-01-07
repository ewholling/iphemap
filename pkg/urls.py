from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = [
    url(r'^home/', views.home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('ipscdb.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
