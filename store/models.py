"""Modeld for store app"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    """Model class for the customer"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(max_length=250, null=True)
    phone = models.CharField(max_length=11, null=True)

    def __str__(self):
        return str(self.name)
    

class Product(models.Model):
    """Model class for products"""
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str(self):
        return str(self.name)
    


class Order(models.Model):
    """Model class for Orders"""
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str(self):
        return str(self.transaction_id)
    

class OrderItem(models.Model):
    """Models for OrderItem"""
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.product)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.address)