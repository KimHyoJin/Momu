from django.conf.urls import url
from test import views

urlpatterns = [
    url(r'^$', views.test_list),
    url(r'^(?P<pk>[0-9]+)/$', views.test_detail),
]