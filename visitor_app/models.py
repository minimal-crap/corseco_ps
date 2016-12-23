from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    whom_to_meet = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos", blank=True)
