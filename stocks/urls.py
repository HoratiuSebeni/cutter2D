from django.urls import path
from . import views

urlpatterns = [
    path('newStockBoard', views.newStockBoard, name='newStockBoard'),
    path('newBoard', views.newBoard, name='newBoard'),
    path('newStockEdge', views.newStockEdge, name='newStockEdge'),
    path('newEdge', views.newEdge, name='newEdge'),
]