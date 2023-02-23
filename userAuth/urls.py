from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name="startPage"),
    path('login', views.loginPage, name="loginPage"),
    path('logout', views.logoutPage, name="logoutPage"),
    path('register', views.registerPage, name="registerPage"),
    path('home', views.homePage, name="homePage"),
]