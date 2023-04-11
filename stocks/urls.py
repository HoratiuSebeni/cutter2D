from django.urls import path
from . import views

urlpatterns = [
    path('newStock', views.newStock, name='newStock'),
    path('newMaterial', views.newMaterial, name='newMaterial'),

]