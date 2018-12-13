from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.datetime_safe import datetime
class Restaurant(models.Model):
    restaurant_name=models.CharField(max_length=120)
    restaurant_description=models.CharField(max_length=150)
    restaurant_address=models.CharField(max_length=120,null=True)
    upload_image_path=models.ImageField(upload_to='mysite')

    def __str__(self):
        return self.restaurant_name

    def get_absolute_url(self):
        return "product/resturent/{{self.id}}/"

class Product_Details(models.Model):

    resturant=models.ForeignKey(Restaurant,related_name='res',on_delete=models.CASCADE)
    product_name=models.CharField(max_length=120)
    product_description=models.TextField()
    product_price=models.DecimalField(decimal_places=2,max_digits=1000)


    def __str__(self):
        return self.product_name

class User_Details(models.Model):
    username=models.CharField(max_length=120)
    password=models.CharField(max_length=120)
    address=models.TextField()
    phone_number=models.DecimalField(decimal_places=0,max_digits=10)
    email=models.EmailField()

    def __str__(self):
        return self.username





class Feedback(models.Model):
    title=models.CharField(max_length=150)
    descriptions=models.TextField()


class Order(models.Model):
    owner=models.ForeignKey(User_Details,on_delete=models.SET_NULL,null=True)


class Cart(models.Model):
    user=models.ForeignKey(User_Details,on_delete=models.CASCADE)
    products=models.ForeignKey(Product_Details,blank=True,null=True,on_delete=models.CASCADE)
    quantity=models.DecimalField(decimal_places=0,max_digits=2)
    unit_total=models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    total=models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)



