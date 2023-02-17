from django.db import models
from .choices import MARITAL_STATUS_CHOICES

class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=150)
    age = models.IntegerField()
    city = models.CharField(max_length=150)
    street_address = models.CharField(max_length=150)
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ["-date_created"]

