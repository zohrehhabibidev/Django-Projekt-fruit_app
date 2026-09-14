from django.db import models

# Create your models here.


class Fruit(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    origin_country = models.CharField(max_length=50, null=True)
