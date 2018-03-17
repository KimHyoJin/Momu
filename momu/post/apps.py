from __future__ import unicode_literals

from django.apps import AppConfig
from django.http import JsonResponse


def upload():
    return JsonResponse({'test': 'result'})


class PostConfig(AppConfig):
    name = 'post'
