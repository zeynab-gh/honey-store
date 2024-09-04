import datetime
from time import timezone
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=22)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}' 


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500,default='', blank=True, null=True)
    price = models.DecimalField(max_digits=12,decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    picture = models.ImageField(upload_to='upload/product/')

    def __str__(self):
        return self.name



class Order(models.Model):
    prouct = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quntity = models.IntegerField(default=1)
    address = models.CharField(max_length=500, blank=False, default='')
    phone = models.CharField(max_length=200, blank=False)
    date = models.DateField(default=datetime.datetime.now())
    statuse = models.BooleanField(default=False)

    def __str__(self):
        return self.prouct