from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from .models import Card, Appliance
from django.urls import reverse

# TODO: Add an edit button for each card and appliance
# TODO: Add searching code

# Main menu view
def mainMenu(request):
	return render(request, 'cards/MainCards.html')

# view for what appliances are on thecard	
def applianceView(request, card_id):
	cards = get_object_or_404(Card, pk=card_id)
	appliances = Appliance.objects.filter(card = cards)
	context = {
		"appliances" : appliances,
		"cards" : cards,
	}
	
	return render(request, 'cards/applianceView.html',context)

def applianceDetails(request, appliance_id):
	appliance = get_object_or_404(Appliance,pk = appliance_id)
	context = {
		"appliance" : appliance,
	}
	return render(request, 'cards/applianceDetails.html',context)


def lookCards(request):

	searched = ''
	modelCheck = 'checked'
	nameCheck = 'unchecked'
	typeCheck = 'unchecked'
	cards = []
	if request.POST == {}:
		cards = Card.objects.order_by('-pub_date')[:20]
	else:
		searched = request.POST['search']
		if searched == '':
			cards = Card.objects.order_by('-pub_date')[:20]
		else:
			if request.POST.get('model'):
				cards += Card.objects.filter(modelNumber__contains = searched )
				modelCheck = 'checked'
			else:
				modelCheck = 'unchecked'
			if request.POST.get('name'):
				cards += Card.objects.filter(brand__contains = searched)
				nameCheck = 'checked'
			else:
				nameCheck = 'unchecked'
			if request.POST.get('type'):
				cards += Card.objects.filter(applianceType__contains = searched)
				typeCheck = 'checked'
			else: 
				typeCheck = 'unchecked'
	
	context = {
		'cards' : cards,
		'search' : searched,
		'modelCheck' : modelCheck,
		'nameCheck' : nameCheck,
		'typeCheck' : typeCheck,
	}

	return render(request, 'cards/lookCards.html', context )

def addCards(request):
	cards = Card.objects.order_by('-pub_date')[:20]
	context = {
		'cards' : cards,
	}
	return render(request, 'cards/addCards.html', context )



	
def lookAppliance(request):

	searched = ''
	appliances = []
	sModel = ''
	sSerial = ''
	sLoadDate = ''
	scrapCheck = ''
	showScrapped = False

	if request.POST == {}:
		appliances = Appliance.objects.order_by("-pub_date")[:40]
	else:
		searched = request.POST['searchText']
		if searched == '':
			appliances = Appliance.objects.order_by('-pub_date')[:40]
			if(request.POST.get('scrap')):
				showScrapped = True
				scrapCheck = "checked"
			
			else:
				showScrapped = False
				scrapCheck = "unchecked"
		else:
			if(request.POST.get('selectSearch')):
				option = request.POST['selectSearch']
				if option == 'model':
					sModel = 'selected'
					appliances = Appliance.objects.filter(card__modelNumber__contains = searched)
				if option == 'serial':
					appliances = Appliance.objects.filter(serialNumber__contains = searched )
					sSerial = 'selected'
				if option == 'loadDate':
					appliances = Appliance.objects.filter(date__contains = searched)
					sLoadDate = 'selected'
			if(request.POST.get('scrap')):
				showScrapped = True
				scrapCheck = "checked"
			
			else:
				showScrapped = False
				scrapCheck = "unchecked"

	context = {
		'appliances' : appliances,
		'sModel' : sModel,
		'sSerial' : sSerial,
		'sLoadDate' : sLoadDate,
		'scrapCheck' : scrapCheck,
		'showScrapped' : showScrapped,
	}


	return render(request, 'cards/lookAppliance.html', context )
	

def newCard(request):
	model = request.POST['model']
	brand = request.POST['brand']
	applianceType = request.POST['type']
	modelCard = Card.objects.filter(modelNumber=model)

	if(model and brand and applianceType ):
		if(not modelCard):
			saveCard = Card(modelNumber = model ,brand= brand ,applianceType = applianceType, pub_date= timezone.now())
			saveCard.save()
		else:
			print("ERROR Card's model already exists")
	return HttpResponseRedirect('/addCards')


def newAppliance(request, card_id):
	card = get_object_or_404(Card, pk=card_id)
	serial = request.POST['serial']
	unitCost = request.POST['unitCost']
	classLevel = request.POST['classLevel']
	color = request.POST['color']
	loadDate = request.POST['loadDate']
	serialAppliance = Appliance.objects.filter(serialNumber = serial)
	if(serial and unitCost and classLevel):
		if(not serialAppliance):
			saveAppliance = Appliance(card = card, serialNumber = serial, unitCost= unitCost, Class= classLevel, pub_date = timezone.now(), color = color, date = loadDate)
			saveAppliance.save()
		else:
			print("ERROR Appliance's serial already exists")
	return redirect('/applianceView/' + str(card_id))

def editAppliance(request, appliance_id):
	appliance = get_object_or_404(Appliance, pk=appliance_id)
	
	if(request.POST['serialNumber'] != ''):
		appliance.serialNumber = request.POST['serialNumber']
	if(request.POST['class'] != ''):
		appliance.Class = request.POST['class']
	if(request.POST['loadDate'] != ''):
		appliance.date = request.POST['loadDate']
	if(request.POST['cost'] != ''):
		appliance.unitCost = request.POST['cost']
	if(request.POST['color'] != ''):
		appliance.color = request.POST['color']
	if(request.POST['dateSold'] != ''):
		appliance.dateSold = request.POST['dateSold']
	if(request.POST['purchaser'] != ''):
		appliance.purchaser = request.POST['purchaser']
	if(request.POST['ticketNum'] != ''):
		appliance.ticketNum = request.POST['ticketNum']
	if(request.POST['sellingPrice'] != ''):
		appliance.sellingPrice = request.POST['sellingPrice']
	if(request.POST.get('scrap')):
		appliance.scrapped = True
	else:
		appliance.scrapped = False

	appliance.save()
	return redirect('/applianceDetails/' + str(appliance_id))

def editCard(request, card_id):
	card = get_object_or_404(Card, pk=card_id)

	print("MADE IT TO EDIT CARD")

	if(request.POST['brand'] != ''):
		card.brand = request.POST['brand']
	if(request.POST['type'] != ''):
		card.applianceType = request.POST['type']
	if(request.POST['model'] != ''):
		card.modelNumber = request.POST['model']
	card.save()
	return redirect('/applianceView/' + str(card_id))

def deleteCard(request, card_id):
	card = get_object_or_404(Card, pk=card_id)
	card.delete()
	return redirect('/addCards')		

def deleteAppliance(request,appliance_id):
	appliance = get_object_or_404(Appliance, pk=appliance_id)
	card = appliance.card
	appliance.delete()
	return redirect('/applianceView/' + str(card.id))

def init(request):
	print('Nuking')
	nuke(request)
	cards = []
	print("nuke Done")
	
	print("making Cards")
	for i in range(1000):
		whirlPool = Card(modelNumber = "WED4916FW" ,brand= "Whirlpool" ,applianceType = "Dryer" , pub_date= timezone.now())
		maytag = Card(modelNumber = "MFB2055FRZ" ,brand= "Maytag" ,applianceType = "Refrigerator" , pub_date= timezone.now())
		lg = Card(modelNumber = "LDE4413ST" ,brand= "LG" ,applianceType = "Electric Range" , pub_date= timezone.now())
		freezer = Card(modelNumber = "MZF34X20DW" ,brand= "Maytag" ,applianceType = "Upright Freezer" , pub_date= timezone.now())
		whirlPool.save()
		maytag.save()
		lg.save()
		freezer.save()
		cards.append(whirlPool)
		cards.append(maytag)
		cards.append(lg)
		cards.append(freezer)


	print("Cards Done")

	print("now Appliances")
	for card in cards:
		for i in range(5):
			if(i%2==0):
				appliance = Appliance(card = card, serialNumber = "W789789"+str(i), unitCost = 100.00, Class = "A", pub_date = timezone.now(), date = "1222A", color = "Stanless Steel", scrapped= True )
				appliance.save()
			
			else:
				appliance = Appliance(card = card, serialNumber = "R456845"+str(i), unitCost = 10.00, Class = "A", pub_date = timezone.now(), date = "11/26/19", color = "Blue" )
				appliance.save()
	print("ALL DONE")

	return redirect('/')

def nuke (request):
	for q in Card.objects.all():
		q.delete()


	
