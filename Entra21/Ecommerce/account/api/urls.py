from django.urls import path
from . import viewsets

app_name = 'account'

"""
Urls da API.
"""

urlpatterns = [
    path('', viewsets.MyUserViewSet.list, name='list'),
    path('/<int:pk>', viewsets.MyUserViewSet.retrieve, name='retrieve'),
]