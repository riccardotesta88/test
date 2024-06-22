from .models import Order, Product
from rest_framework import serializers

'''Struttura dei dati da serializzare in json'''


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['ID', 'name','price']

class OrderSerializer(serializers.ModelSerializer):
    # Serializzare le chiavi dei prodotti associati
    products_items=ProductSerializer(many=True,read_only=True)

    class Meta:
        model = Order
        fields = ['ID', 'name', 'description', 'date','products','products_items']

