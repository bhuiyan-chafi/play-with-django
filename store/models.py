from django.db import models
from customer.models import Customer

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    #promotion = models.ManyToManyField("Promotion", related_name='product')
    #related_name will create the column with exact same name but if we don't use it then django will create the field name automatically. This default convention is the best because if we choose our names then we have to follow it everywhere.

    promotion = models.ManyToManyField("Promotion")
    #you might be wondering why we have written the Promotion class in " ", its because the class has been defined after the product class so we have indicated to look for a class that is called "Promotion"

class Promotion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    discount = models.FloatField()
    
class Order(models.Model):
    PENDING = 'P'
    COMPLETE = 'C'
    FAILED = 'F'

    PAYMENT_STATUS = [
        (PENDING,'Pending'),
        (COMPLETE,'Complete'),
        (FAILED,'Failed'),
    ]
    ORDER_STATUS = [
        (PENDING,'Pending'),
        (COMPLETE,'Complete'),
        (FAILED,'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS,default=PENDING)
    order_status = models.CharField(max_length=1,choices=ORDER_STATUS,default=PENDING)

class OrderedProucts(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price_ordered_at = models.DecimalField(max_digits=6,decimal_places=2)