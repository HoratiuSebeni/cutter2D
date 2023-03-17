from django.db import models
from userAuth.models import Company

# Create your models here.

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    colorCode = models.TextField(null=False, blank=False)
    colorName = models.TextField()
    brand = models.TextField(null=False, blank=False)
    material = models.CharField(default='PAL', max_length=20, null=False, blank=False)
    dimensionHeight = models.IntegerField(default=2800)
    dimensionLength = models.IntegerField(default=2070)
    dimensionWidth = models.IntegerField(default=18)
    photo = models.ImageField(null=True, blank=True)
    author = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        unique_together = ('colorCode', 'brand', 'material')
        ordering = ['id', 'brand', 'material', 'colorCode']

class StockBoard(models.Model):
    id = models.AutoField(primary_key=True)
    companyName = models.ForeignKey(Company, on_delete=models.CASCADE)
    idBoard = models.ForeignKey(Board, on_delete=models.CASCADE)
    noPieces = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    class Meta:
        unique_together = ('companyName', 'idBoard')
        ordering = ['id', 'companyName', 'idBoard']


class Edge(models.Model):
    id = models.AutoField(primary_key=True)
    colorCode = models.TextField(null=False, blank=False)
    brand = models.TextField(null=False, blank=False)
    length = models.IntegerField(null=False, blank=False)
    width = models.IntegerField(null=False, blank=False)
    colorName = models.TextField()
    photo = models.ImageField(null=True, blank=True)
    author = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        unique_together = ('colorCode', 'brand', 'length', 'width')
        ordering = ['id', 'colorCode', 'length', 'width']

class StockEdge(models.Model):
    id = models.AutoField(primary_key=True)
    companyName = models.ForeignKey(Company, on_delete=models.CASCADE)
    idEdge = models.ForeignKey(Edge, on_delete=models.CASCADE)
    noMeters = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    class Meta:
        unique_together = ('companyName', 'idEdge')
        ordering = ['id', 'companyName', 'idEdge']