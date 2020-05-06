from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=10, null=False, unique=True)
    ville = models.CharField(max_length=25, null=False)


class DeleveryPerson(CustomUser):
    code = models.CharField(max_length=10, null=False, unique=True)
