from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name="start"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutPage, name="logout"),
    path('register', views.registerPage, name="register"),
    path('home', views.homePage, name="home")
]