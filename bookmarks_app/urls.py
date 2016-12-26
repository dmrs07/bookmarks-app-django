from django.conf.urls import include, url
from django.contrib import admin
from bookmarks_application import urls as app_urls
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views as django_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(app_urls)),
     url(r'^login/$', django_views.login, {'template_name': 'login.html'},
        name='app_login'),
    url(r'^logout/$', django_views.logout,
        {'next_page': reverse_lazy('bookmark_list')}, name='app_logout'),
]