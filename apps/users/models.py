from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Employee(AbstractUser):
    legalId = models.BigIntegerField()
    age = models.IntegerField()
    hireDate = models.DateField()
    def __str__(self):
        return self.username