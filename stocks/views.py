from django.shortcuts import render, redirect
from .models import StockBoard, Board, StockEdge, Edge
from django.contrib import messages
from django.db.models import F
from userAuth.models import CompanyEmployer
# Create your views here.

def newStockBoard(request):
    user = request.user
    companyName = CompanyEmployer.objects.get(user=user)
    if request.method == 'POST':
        try:
            id = Board.objects.filter(colorCode=request.POST.get('colorCode'), brand=request.POST.get('brand'), material=request.POST.get('material')).get()
            if StockBoard.objects.filter(companyName=companyName, idBoard=id):
                updateStockBoard(request)
            else:
                StockBoard.objects.create(companyName=companyName, idBoard=id, noPieces=request.POST.get('noPieces'), price=request.POST.get('price'))
                messages.error(request, 'The item was added succesfuly!')
                return redirect(newStockBoard)
        except:
            messages.error(request, 'Something went wrong. Maybe the item you try to add does not exist in the standard boards list. Please try to add it first in the boards list and then ty again!')

    return render(request, 'stocks/newStockBoard.html')

def updateStockBoard(request):
    user = request.user
    companyName = CompanyEmployer.objects.get(user=user)
    if request.method == 'POST':
        try:
            id = Board.objects.filter(colorCode=request.POST.get('colorCode'), brand=request.POST.get('brand'), material=request.POST.get('material')).get()
            StockBoard.objects.filter(companyName=companyName, idBoard=id).update(
                noPieces = F('noPieces') + request.POST.get('noPieces')
            )
            if request.POST.get('price'):
                StockBoard.objects.filter(companyName=companyName, idBoard=id).update(price=request.POST.get('price'))
            
            messages.error(request, 'The stock was updated succesfuly!')
        except:
            messages.error(request, 'Someting went wrong. The item was not updated! Please try again!')
        
    return render(request, 'stocks/newStockBoard.html')

def newBoard(request):
    user = request.user
    companyName = CompanyEmployer.objects.get(user=user)
    if request.method == 'POST':
        try:
            Board.objects.create(colorCode=request.POST.get('colorCode'), colorName=request.POST.get('colorName'), brand=request.POST.get('brand'), material=request.POST.get('material'), dimensionHeight=request.POST.get('height'), dimensionLength=request.POST.get('length'), dimensionWidth=request.POST.get('width'), photo=request.POST.get('photo'), author=companyName)
            messages.error(request, 'You added successfuly a new board to the database! Congratulations!')
        except:
            messages.error(request, 'The board you try to add to de list already exist. Try to add it to your personal stock or update your stock!')

    return render(request, 'stocks/newBoard.html')

def newStockEdge(request):
    user = request.user
    companyName = CompanyEmployer.objects.get(user=user)
    if request.method == 'POST':
        try:
            id = Edge.objects.filter(colorCode=request.POST.get('colorCode'), brand=request.POST.get('brand'), length=request.POST.get('length'), width=request.POST.get('width')).get()
            if StockEdge.objects.filter(companyName=companyName, idEdge=id):
                updateStockEdge(request)
            else:
                StockEdge.objects.create(companyName=companyName, idEdge=id, noMeters=request.POST.get('noMeters'), price=request.POST.get('price'))
                messages.error(request, 'The item was added succesfuly!')
                return redirect(newStockEdge)
        except:
            messages.error(request, 'Something went wrong. Maybe the item you try to add does not exist in the standard edge list. Please try to add it first in the egde list and then ty again!')

    return render(request, 'stocks/newStockEdge.html')

def updateStockEdge(request):
    user = request.user
    companyName = CompanyEmployer.objects.get(user=user)
    if request.method == 'POST':
        try:
            id = Edge.objects.filter(colorCode=request.POST.get('colorCode'), brand=request.POST.get('brand'), length=request.POST.get('length'), width=request.POST.get('width')).get()
            StockEdge.objects.filter(companyName=companyName, idEdge=id).update(
                noMeters = F('noMeters') + request.POST.get('noMeters')
            )
            if request.POST.get('price'):
                StockEdge.objects.filter(companyName=companyName, idEdge=id).update(price=request.POST.get('price'))
            
            messages.error(request, 'The stock was updated succesfuly!')
        except:
            messages.error(request, 'Someting went wrong. The item was not updated! Please try again!')
        
    return render(request, 'stocks/newStockEdge.html')

def newEdge(request):
    user = request.user
    companyName = CompanyEmployer.objects.get(user=user)
    if request.method == 'POST':
        try:
            Edge.objects.create(colorCode=request.POST.get('colorCode'), colorName=request.POST.get('colorName'), brand=request.POST.get('brand'), length=request.POST.get('length'), width=request.POST.get('width'), photo=request.POST.get('photo'), author=companyName)
            messages.error(request, 'You added successfuly a new edge to the database! Congratulations!')
        except:
            messages.error(request, 'The egde you try to add to de list already exist. Try to add it to your personal stock or update your stock!')

    return render(request, 'stocks/newEdge.html')

