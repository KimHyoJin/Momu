from django.conf.urls import url, include
from django.contrib import admin

from momu.post import apps

urlpatterns = [
    url('upload', apps.upload, name='upload'),
]
