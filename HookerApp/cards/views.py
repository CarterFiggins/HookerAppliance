from django.shortcuts import render
from django.http import HttpResponse


def mainMenu(request):
    return render(request, 'cards/MainCards.html')
def lookCards(request):
    return render(request, 'cards/lookCards.html' )
def addCards(request):
    return render(request, 'cards/addCards.html' )
def lookAppliance(request):
    return render(request, 'cards/lookAppliance.html' )
    



