from datetime import date
from django.db import models
from passlib.hash import pbkdf2_sha256

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    password=models.CharField(max_length = 256)
    usertype=models.CharField(max_length=100)
    date = models.DateTimeField()
    
    def verifypassword(self,raw_password):
        print('verify password')
        return pbkdf2_sha256.verify(raw_password,self.password)

    def __str__(self):
        return self.name


class Products(models.Model):
        srno=models.IntegerField()
        images=models.ImageField()
        productname=models.CharField(max_length=100)
        price=models.FloatField()
        totalquantity=models.IntegerField()
        remainingquantity = models.IntegerField()
        status=models.CharField(max_length=100)
        date = models.DateTimeField()
        
        def __str__(self):
            return self.productname


class UserCart(models.Model):
    orderid=models.IntegerField()
    productid=models.IntegerField()
    userid=models.IntegerField()
    quantity=models.IntegerField()
    

        