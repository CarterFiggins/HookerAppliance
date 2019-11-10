from django.urls import path

from . import views

app_name = 'cards'

urlpatterns = [
    path('', views.mainMenu, name='mainMenu'),
    path('lookCards', views.lookCards, name='lookCards'),
    path('addCards', views.addCards, name= 'addCards'),
    path('lookAppliance', views.lookAppliance, name='lookAppliance'),
    path('newCard',views.newCard, name='newCard'),
]