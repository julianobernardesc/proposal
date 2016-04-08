from django.conf.urls import url
from proposal.core import views as c

urlpatterns = [
    url(r'^$', c.home, name='home'),
    url(r'^person/$', c.PersonList.as_view(), name='person_list'),
    url(r'^person/add/$', c.person_create, name='person_add'),
    url(r'^person/(?P<pk>\d+)/$', c.person_detail, name='person_detail'),
    url(r'^person/(?P<pk>\d+)/edit/$', c.person_update, name='person_edit'),
    url(r'^person/(?P<pk>\d+)/delete/$', c.person_delete, name='person_delete'),
]
