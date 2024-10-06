from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)


#Платіжна система
class Order(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)