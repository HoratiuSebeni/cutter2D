from django.urls import path
from . import views
from userAuth.views import homePage

urlpatterns = [
    path('newStock', views.newStock, name='newStock'),
    path('newBoard', views.newBoard, name='newBoard'),
]