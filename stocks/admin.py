from django.contrib import admin
from .models import Material, Stock
# Register your models here.

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'material', 'colorCode', 'length', 'width')

class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'companyName', 'idMaterial', 'noPieces')

admin.site.register(Material, MaterialAdmin)
admin.site.register(Stock, StockAdmin)