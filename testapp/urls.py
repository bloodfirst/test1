from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'testapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'testapp.views.welcomepage'),
    url(r'^admin/', include(admin.site.urls)),
]
