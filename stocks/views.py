from django.shortcuts import render, redirect
from .models import StockBoard, Board
from userAuth.models import UserDetails
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import F
# Create your views here.

def newStock(request):
    user = request.user
    if request.method == 'POST':
        try:
            Board.objects.get(colorCode=request.POST.get('colorCode')).colorCode
            if StockBoard.objects.filter(companyEmail=user, colorCode=Board.objects.get(colorCode=request.POST.get('colorCode'))):
                updateStock(request)
            else:
                StockBoard.objects.create(companyEmail=user, colorCode=Board.objects.get(colorCode=request.POST.get('colorCode')), noPieces=request.POST.get('noPieces'), price=request.POST.get('price'))
                messages.error(request, 'The item was added succesfuly!')
                return redirect(newStock)
        except:
            messages.error(request, 'Something went wrong. Maybe the item you try to add does not exist in the stock. Please try to add it first in the stock table!')

    return render(request, 'stocks/newStock.html')

def updateStock(request):
    user = request.user
    if request.method == 'POST':
        try:
            StockBoard.objects.filter(companyEmail=user, colorCode=Board.objects.get(colorCode=request.POST.get('colorCode'))).update(
                noPieces = F('noPieces') + request.POST.get('noPieces')
            )
            if request.POST.get('price'):
                StockBoard.objects.filter(companyEmail=user, colorCode=Board.objects.get(colorCode=request.POST.get('colorCode'))).update(price=request.POST.get('price'))
            
            messages.error(request, 'The stock was updated succesfuly!')
        except:
            messages.error(request, 'Someting went wrong. The item was not updated! Please try again!')
        
    return render(request, 'stocks/newStock.html')

def newBoard(request):
    user = request.user
    if request.method == 'POST':
        try:
            Board.objects.create(colorCode=request.POST.get('colorCode'), colorName=request.POST.get('colorName'), brand=request.POST.get('brand'), material=request.POST.get('material'), dimensionHeight=request.POST.get('height'), dimensionLength=request.POST.get('length'), dimensionWidth=request.POST.get('width'), photo=request.POST.get('photo'))
            messages.error(request, 'You added successfuly a new board to the database! Congratulations!')
        except:
            messages.error(request, 'The board you try to add to de list already exist. Try to add it to your personal stock or update your stock!')

    return render(request, 'stocks/newBoard.html')
