from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    colorCode = models.TextField(null=False, blank=False)
    colorName = models.TextField()
    brand = models.TextField(null=False, blank=False)
    material = models.CharField(default='PAL', max_length=20, null=False, blank=False)
    dimensionHeight = models.IntegerField(default=2800)
    dimensionLength = models.IntegerField(default=2070)
    dimensionWidth = models.IntegerField(default=18)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.colorCode
    
    class Meta:
        unique_together = ('colorCode', 'brand', 'material')
        ordering = ['brand', 'material', 'colorCode']

class StockBoard(models.Model):
    companyEmail = models.ForeignKey(User, on_delete=models.CASCADE)
    colorCode = models.ForeignKey(Board, on_delete=models.CASCADE)
    noPieces = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    class Meta:
        unique_together = ('companyEmail', 'colorCode')
        ordering = ['companyEmail', 'colorCode']