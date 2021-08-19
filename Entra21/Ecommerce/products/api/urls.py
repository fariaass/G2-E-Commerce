from products.api.viewsets import ProductViewSet
from django.urls import path

app_name = 'products'

"""
Api and application urls
"""

urlpatterns = [
    path('', ProductViewSet.list, name='list')
]