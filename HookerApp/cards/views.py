from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from .models import Card, Appliance
from django.urls import reverse


def mainMenu(request):
	return render(request, 'cards/MainCards.html')

		
def applianceView(request, card_id):
	cards = get_object_or_404(Card, pk=card_id)
	appliances = Appliance.objects.filter(card = cards)
	context = {
		"appliances" : appliances,
		"cards" : cards,
	}
	
	return render(request, 'cards/applianceView.html',context)



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
		saveCard = Card(modelNumber = model ,brand= brand ,applianceType = applianceType, pub_date= timezone.now())
		saveCard.save()
		print("SUCCESS")
	else:
		print("FAILD")
	return HttpResponseRedirect('/addCards')


def newAppliance(request, card_id):
	card = get_object_or_404(Card, pk=card_id)
	serial = request.POST['serial']
	unitCost = request.POST['unitCost']
	classLevel = request.POST['classLevel']
	if(serial and unitCost and classLevel):
		saveAppliance = Appliance(card = card, serialNumber = serial, unitCost= unitCost, Class= classLevel, pub_date = timezone.now())
		saveAppliance.save()
	return redirect('/applianceView/' + str(card_id))
		


def init(request):
	nuke(request)
	for i in range(5):
		card = Card(modelNumber = "MODEL" ,brand= "BRAND" ,applianceType = "TYPE" , pub_date= timezone.now())
		card.save()
		appliance = Appliance(card = card, serialNumber = "SERIAL", unitCost = 10.00, Class = "A CLASS", pub_date = timezone.now())
		appliance.save()
	return redirect('/')

def nuke (request):
	for q in Card.objects.all():
		q.delete()


	