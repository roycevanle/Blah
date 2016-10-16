from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'guest_sorter/$', TemplateView.as_view(template_name='resource_finder/guest_sorter.html'), name='guest_sorter'),
    url(r'get/primary_needs/$', views.primary_needs, name='primary_needs'),

]
