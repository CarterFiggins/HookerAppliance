from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from .models import Card, Appliance
from django.urls import reverse

# TODO: Add an edit button for each card and appliance
# TODO: Add searching code


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


# has same one in it duplicets
def lookCards(request):

	searched = ''
	modelCheck = 'checked'
	nameCheck = 'unchecked'
	typeCheck = 'unchecked'
	cards = []
	if request.POST == {}:
		cards = Card.objects.all()
	else:
		searched = request.POST['search']
		if searched == '':
			cards = Card.objects.all()
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
	cards = Card.objects.all()
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

	if request.POST == {}:
		print('HELLO')
		appliances = Appliance.objects.filter(serialNumber__contains = searched)
	else:
		print("GOT INFO YESSS")

		print('INFO IS: ', request.POST)

		searched = request.POST['searchText']
		if searched == '':
			appliances = Appliance.objects.all()

		if(request.POST.get('selectSearch')):
			option = request.POST['selectSearch']
			if option == 'model':
				pass
			if option == 'serial':
				appliances = Appliance.objects.filter(serialNumber__contains = searched )
				sSerial = 'selected'
			if option == 'loadDate':
				appliances = Appliance.objects.filter(date__contains = searched)
				sLoadDate = 'selected'


	context = {
		'appliances' : appliances,
		'sModel' : sModel,
		'sSerial' : sSerial,
		'sLoadDate' : sLoadDate,
	}


	return render(request, 'cards/lookAppliance.html', context )
	

def newCard(request):
	model = request.POST['model']
	brand = request.POST['brand']
	applianceType = request.POST['type']
	if(model and brand and applianceType ):
		saveCard = Card(modelNumber = model ,brand= brand ,applianceType = applianceType, pub_date= timezone.now())
		saveCard.save()
	return HttpResponseRedirect('/addCards')


def newAppliance(request, card_id):
	card = get_object_or_404(Card, pk=card_id)
	serial = request.POST['serial']
	unitCost = request.POST['unitCost']
	classLevel = request.POST['classLevel']
	color = request.POST['color']
	loadDate = request.POST['loadDate']
	if(serial and unitCost and classLevel):
		saveAppliance = Appliance(card = card, serialNumber = serial, unitCost= unitCost, Class= classLevel, pub_date = timezone.now(), color = color, date = loadDate)
		saveAppliance.save()
	return redirect('/applianceView/' + str(card_id))
		


def init(request):
	nuke(request)
	cards = []
	
	for i in range(20):
		cards.append(Card(modelNumber = "WED4916FW" ,brand= "Whirlpool" ,applianceType = "Dryer" , pub_date= timezone.now()))
		cards.append(Card(modelNumber = "MFB2055FRZ" ,brand= "Maytag" ,applianceType = "Refrigerator" , pub_date= timezone.now()))
		cards.append(Card(modelNumber = "LDE4413ST" ,brand= "LG" ,applianceType = "Electric Range" , pub_date= timezone.now()))
		cards.append(Card(modelNumber = "MZF34X20DW" ,brand= "Maytag" ,applianceType = "Upright Freezer" , pub_date= timezone.now()))


	for card in cards:
		card.save()
		for i in range(5):
			appliance = Appliance(card = card, serialNumber = "R456845", unitCost = 10.00, Class = "A CLASS", pub_date = timezone.now(), date = "11/26/19", color = "Blue" )
			appliance.save()

	return redirect('/')

def nuke (request):
	for q in Card.objects.all():
		q.delete()


	
