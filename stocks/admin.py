from django.contrib import admin
from .models import Board, StockBoard, Edge, StockEdge
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'material', 'colorCode')

class StockBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'companyEmail', 'idBoard', 'noPieces')

class EdgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'colorCode', 'length', 'width')

class StockEdgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'companyEmail', 'idEdge', 'noMeters')

admin.site.register(Board, BoardAdmin)
admin.site.register(StockBoard, StockBoardAdmin)
admin.site.register(Edge, EdgeAdmin)
admin.site.register(StockEdge, StockEdgeAdmin) 