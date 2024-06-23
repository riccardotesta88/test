

from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Order,Product
from ..serializers import OrderSerializer, ProductSerializer

class OrderSerializerTest(TestCase):
    def setUp(self):
        '''Operazioni preliminiari pre test'''
        self.order_attr={'name': 'proda', 'description': ''}
        self.prod_attr={'name': 'prd_22', 'price': '55.99'}
        self.serialized_data={'name': 'proda', 'description': ''}


    def test_serializer_order(self):
        '''Verifica dei dati serializzati dalle classi del modello Order'''
        #Verifica creazione nuovo oggetto

        order = Order.objects.create(**self.order_attr)
        order.products.add(Product.objects.create(**self.prod_attr))
        serializer = OrderSerializer(instance=order)
        data = serializer.data
        print(data)
        #Controllo campi
        self.assertEqual(set(data.keys()), set(['ID','date','products','name', 'description']))


    def test_serializer_product(self):
        '''Verifica dei dati serializzati dalle classi del modello Procuct'''
        product_data = Product.objects.first()
        product_serializer = ProductSerializer(instance=product_data)
        data = product_serializer.data
        self.assertEqual(set(data.keys()), set(['name','price']))