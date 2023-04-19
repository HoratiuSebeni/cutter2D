from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name="start"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutPage, name="logout"),
    path('register', views.registerPage, name="register"),
    path('home', views.homePage, name="home"),
    path('account', views.myAccount, name='account'),
    path('changePassword', views.changePassword, name='changePassword'),
    path('updateName', views.updateName, name='updateName'),
    path('updateCompanyDetails', views.updateCompanyDetails, name='updateCompanyDetails'),
    path('createEmployer', views.createEmployer, name='createEmployer'),
]