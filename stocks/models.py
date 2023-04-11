from django.db import models
from userAuth.models import Company

# Create your models here.

class Material(models.Model):
    id = models.AutoField(primary_key=True)
    colorCode = models.TextField(null=False, blank=False)
    colorName = models.TextField()
    brand = models.TextField(null=False, blank=False)
    material = models.CharField(max_length=20, null=False, blank=False)
    height = models.IntegerField(default=1000, null=False, blank=False)
    length = models.IntegerField(null=False, blank=False)
    width = models.IntegerField(null=False, blank=False)
    photo = models.ImageField(null=True, blank=True)
    author = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        unique_together = ('colorCode', 'brand', 'material', 'length', 'width')
        ordering = ['id', 'brand', 'material', 'colorCode', 'length', 'width']

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    companyName = models.ForeignKey(Company, on_delete=models.CASCADE)
    idMaterial = models.ForeignKey(Material, on_delete=models.CASCADE)
    noPieces = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    class Meta:
        unique_together = ('companyName', 'idMaterial')
        ordering = ['id', 'companyName', 'idMaterial']
