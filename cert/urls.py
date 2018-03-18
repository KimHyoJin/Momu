"""
from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^$', views.UserViewSet, name='cert_login'),
    # url(r'^/join$', views.join, name='cert_join'),
]
"""