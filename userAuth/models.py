from django.contrib.auth.models import User
from django.db import models

class Company(models.Model):
    company = models.TextField(primary_key=True)
    country = models.TextField()
    city = models.TextField()
    adress = models.TextField()
    phone = models.IntegerField()
    companyType = models.CharField(max_length=20, null=False, blank=False)

    def __str__ (self):
        return str(self.company)


class CompanyEmployer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False, blank=False)
    name = models.TextField(null=True, blank=True)
    middleName=models.TextField(null=True, blank=True)
    accountPermisions = models.CharField(max_length=20, default='admin')
