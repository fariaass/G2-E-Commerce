from cart.api.viewsets import CartViewSet
from django.urls import path

app_name = 'cart'

"""
Api and application urls
"""

urlpatterns = [
    path('', CartViewSet.list, name='list')    
]