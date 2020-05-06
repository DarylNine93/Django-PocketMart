from django.db import models
from Categories.models import Category


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    regular_price = models.FloatField()
    promotional_price = models.FloatField(default=0.0)
    weight = models.FloatField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
