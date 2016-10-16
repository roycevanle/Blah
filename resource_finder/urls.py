from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'guest_sorter/$', TemplateView.as_view(template_name='resource_finder/guest_sorter.html'), name='guest_sorter'),
    url(r'get/primary_needs/$', views.primary_needs, name='primary_needs'),
    url(r'get/list_facilities/$', views.list_relevant_facilities, name='list_relevant_facilities'),

    url(r'facility/create_account/$', views.create_account, name='create_account'),
    url(r'facility/view/(?P<facility_id>[\d+])/$', views.view_facility, name='view_facility'),
    url(r'give/$', views.give_to_facility, name='give_list'),
]
