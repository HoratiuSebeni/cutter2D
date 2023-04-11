from django.shortcuts import render, redirect
from .models import Material, Stock
from django.contrib import messages
from django.db.models import F
from userAuth.models import Company, CompanyEmployer
# Create your views here.

def newStock(request):
    user = request.user
    if request.method == 'POST':
        userCompany = CompanyEmployer.objects.get(user=user).company
        companyName = Company.objects.get(company=userCompany)
        try:
            id = Material.objects.filter(colorCode=request.POST.get('colorCode'), brand=request.POST.get('brand'), material=request.POST.get('material')).get()
            if Stock.objects.filter(companyName=companyName, idMaterial=id):
                updateStock(request)
            else:
                Stock.objects.create(companyName=companyName, idMaterial=id, noPieces=request.POST.get('noPieces'), price=request.POST.get('price'))
                messages.error(request, 'The item was added succesfuly!')
                return redirect(newStock)
        except:
            messages.error(request, 'Something went wrong. Maybe the item you try to add does not exist in the standard item list. Please try to add it first in the list and then ty again!')

    return render(request, 'stocks/newStockBoard.html')

def updateStock(request):
    user = request.user
    if request.method == 'POST':
        userCompany = CompanyEmployer.objects.get(user=user).company
        companyName = Company.objects.get(company=userCompany)
        try:
            id = Material.objects.filter(colorCode=request.POST.get('colorCode'), brand=request.POST.get('brand'), material=request.POST.get('material')).get()
            Stock.objects.filter(companyName=companyName, idMaterial=id).update(
                noPieces = F('noPieces') + request.POST.get('noPieces')
            )
            if request.POST.get('price'):
                Stock.objects.filter(companyName=companyName, idMaterial=id).update(price=request.POST.get('price'))
            
            messages.error(request, 'The stock was updated succesfuly!')
        except:
            messages.error(request, 'Someting went wrong. The item was not updated! Please try again!')
        
    return render(request, 'stocks/newStockBoard.html')

def newMaterial(request):
    user = request.user
    if request.method == 'POST':
        userCompany = CompanyEmployer.objects.get(user=user).company
        companyName = Company.objects.get(company=userCompany)
        try:
            Material.objects.create(colorCode=request.POST.get('colorCode'), colorName=request.POST.get('colorName'), brand=request.POST.get('brand'), material=request.POST.get('material'), height=request.POST.get('height'), length=request.POST.get('length'), width=request.POST.get('width'), photo=request.POST.get('photo'), author=companyName)
            messages.error(request, 'You added successfuly a new item to the database! Congratulations!')
        except:
            messages.error(request, 'The item you try to add to de list already exist. Try to add it to your personal stock or update your stock!')

    return render(request, 'stocks/newBoard.html')


