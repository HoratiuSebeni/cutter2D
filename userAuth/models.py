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
    company = models.TextField(null=False, blank=False, unique=True)
    accountType = models.CharField(max_length=20, null=False, blank=False)
    accountPermisions = models.CharField(max_length=20, default='admin')

    def __str__ (self):
        return self.user.email


class ChildUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company = models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=False, blank=False)
    name = models.TextField()
    middleName=models.TextField()
    accountPermisions = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.user.email