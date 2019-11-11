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
	cards = []
	cards.append(Card(modelNumber = "WED4916FW" ,brand= "Whirlpool" ,applianceType = "Dryer" , pub_date= timezone.now()))
	cards.append(Card(modelNumber = "MFB2055FRZ" ,brand= "Maytag" ,applianceType = "Refrigerator" , pub_date= timezone.now()))
	cards.append(Card(modelNumber = "LDE4413ST" ,brand= "LG" ,applianceType = "Electric Range" , pub_date= timezone.now()))
	cards.append(Card(modelNumber = "MZF34X20DW" ,brand= "Maytag" ,applianceType = "Upright Freezer" , pub_date= timezone.now()))


	for card in cards:
		card.save()
		for i in range(5):
			appliance = Appliance(card = card, serialNumber = "R456845", unitCost = 10.00, Class = "A CLASS", pub_date = timezone.now())
			appliance.save()

	return redirect('/')

def nuke (request):
	for q in Card.objects.all():
		q.delete()


	