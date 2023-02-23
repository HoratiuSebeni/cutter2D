from django.contrib.auth.models import User
from django.db import models

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.TextField()
    middleName = models.TextField()
    country = models.TextField()
    city = models.TextField()
    adress = models.TextField()
    phone = models.IntegerField()
    company = models.TextField()
    accountType = models.TextField()
    accountPermisions = models.TextField(default='admin')
