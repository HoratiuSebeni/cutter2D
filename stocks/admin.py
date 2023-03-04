from django.contrib import admin
from .models import Board, StockBoard
# Register your models here.

class StockBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'companyEmail', 'colorCode', 'noPieces')

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'material', 'colorCode')

admin.site.register(Board, BoardAdmin)
admin.site.register(StockBoard, StockBoardAdmin)