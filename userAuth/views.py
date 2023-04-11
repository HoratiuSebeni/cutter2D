from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .models import Company, CompanyEmployer
from .forms import CompanyForm, CompanyEmployerForm, UserForm,PasswordForm


def start(request):
    return render(request, 'start.html')

def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('emailLogin')
        password = request.POST.get('passwordLogin')

        try:
            username = User.objects.get(email=email).username
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(homePage)
            else:
                messages.error(request, 'Email or password inccorect')
        except:
            messages.error(request, 'Email or password inccorect')
            
    return render(request, 'userAuth/login.html')

def logoutPage(request):
    logout(request)
    return redirect(start)

def registerPage(request):
    if request.method == 'POST':
        email = request.POST.get('emailRegister')
        password = request.POST.get('passwordRegister')
        username = email
        
        try: 
            user = User.objects.create_user(username, email, password)
            user.save()
            Company.objects.create(company=request.POST.get('companyRegister'), country=request.POST.get('countryRegister'), city=request.POST.get('cityRegister'), adress=request.POST.get('adressRegister'), phone=request.POST.get('phoneRegister'), companyType=request.POST.get('companyType'))
            CompanyEmployer.objects.create(user=user, company=Company.objects.get(company=request.POST.get('companyRegister')))
            login(request, user)
            return redirect (homePage)
        except:
            messages.error(request, 'Can not register the new company. The company maybe already exist')
    
    context = {}
    return render(request, 'userAuth/register.html', context)

@login_required(login_url=loginPage)
def homePage(request):
    return render(request, 'userAuth/home.html')

@login_required(login_url=loginPage)
def myAccount(request):
    companyEmployer = CompanyEmployer.objects.get(user=request.user)
    company = Company.objects.get(company=companyEmployer.company)
    context = {'companyEmployer' : companyEmployer, 'company' : company}
    return render(request, 'userAuth/account.html', context)

def changePassword(request):
    response = "Can not modify your password"
    if request.method == 'POST':
        try:
            user = request.user
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
            response = "Your password was changed"
        except:
            response = "Something went wrong"
    return JsonResponse(response, safe=False)