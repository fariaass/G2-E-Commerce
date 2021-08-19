from django.db import models
from account.models import MyUser
from products.models import Product

class Cart(models.Model):
    """
    Cart model with the respective fields.

    Each user only can have one cart, and one cart only can have one user.
    """
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='cart')
    produtos = models.ManyToManyField(Product, related_name='products')
    