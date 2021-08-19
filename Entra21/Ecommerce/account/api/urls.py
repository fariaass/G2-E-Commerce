from django.urls import path
from . import viewsets

app_name = 'account'

"""
Api and application urls
"""

urlpatterns = [
    path('', viewsets.MyUserViewSet.list, name='list'),
]