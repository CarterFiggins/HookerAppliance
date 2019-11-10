from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from .models import Card, Appliance
from django.urls import reverse


def mainMenu(request):
	return render(request, 'cards/MainCards.html')


def lookCards(request):
	cards = Card.objects.all()
	context = {
		'cards' : cards,
	}

	return render(request, 'cards/lookCards.html', context )

def addCards(request):
	cards = Card.objects.all()
	context = {
		'cards' : cards,
	}
	return render(request, 'cards/addCards.html', context )

	
def lookAppliance(request):
	return render(request, 'cards/lookAppliance.html' )
	

def newCard(request):
	model = request.POST['model']
	brand = request.POST['brand']
	applianceType = request.POST['type']
	print(model)
	if(model and brand and applianceType ):
		saveCard = Card(modelNumber = model ,brand= request.POST['brand'] ,applianceType = request.POST['type'] , pub_date= timezone.now())
		saveCard.save()
		print("SUCCESS")
	else:
		print("FAILD")
	# context = {
	#     "saveCard" : saveCard,
	#     "saved" : True,
	# }
	

	return HttpResponseRedirect('/addCards')

def init(request):
	nuke(request)


def nuke (request):
	for q in Card.objects.all():
		q.delete()
	