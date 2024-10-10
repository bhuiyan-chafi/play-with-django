from django.db import models

class Customer(models.Model):
    #this is what we did in enumeration in php
    BRONZE = 'B'
    SILVER = 'S'
    GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (BRONZE,'Bronze'),
        (SILVER,'Silver'),
        (GOLD,'Gold')
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255,unique=True)
    status = models.BooleanField(default=True)
    membership_type = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=BRONZE)
    #this part is written just to demonstrate the circular dependecy issues
    #address = models.OneToOneField('Address',on_delete=models.CASCADE,related_name="+")

class Address(models.Model):
    street = models.CharField(max_length=255)
    civic = models.PositiveIntegerField()
    cap = models.PositiveIntegerField()
    comune = models.CharField(max_length=2)
    city = models.CharField(max_length=255)
    #we are assuming that one customer can have one address, but the real scenario is different because one address can belong to many customers
    #customer = models.ForeignKey(Customer,on_delete=models.PROTECT,related_name="+")
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

