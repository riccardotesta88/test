from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views

from .viste import view1

router = routers.DefaultRouter()
# Elenco ordini e filtro
router.register(r'orders',view1.OrderItems)
router.register(r'products',view1.ProductItems)


urlpatterns = [
    path('ord/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]+router.urls

