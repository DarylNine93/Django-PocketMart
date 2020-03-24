from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
