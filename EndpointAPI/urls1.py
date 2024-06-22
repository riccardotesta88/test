from django.contrib import admin
from django.urls import path,include
from EndpointAPI.viste import views as viste

''' Servizio rest base'''

urlpatterns = [
    # lista completa
    path("order/",viste.filter,name='ordini'),
    path("order/<int:id>",viste.order,name='detail'),
]
