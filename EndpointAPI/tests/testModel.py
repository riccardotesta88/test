# from django.test import TestCase
from ..models import Order,Product

from django.test import TestCase
from ..serializers import OrderSerializer,ProductSerializer

class OrderSerializerTest(TestCase):
    '''Serializzazione delle voci del modello Order'''
    def setUp(self):
        self.order_attr={'name': 'proda', 'description': ''}

        self.order = Order.objects.create(**self.order_attr)
        self.serializer = OrderSerializer(instance=self.order)

    def test_serializer_valid_data(self):
        '''Serializzazione delle voci del modello Order'''
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set([f.name for f in self.order._meta.get_fields()]))

class OrderModelTest(TestCase):
    def setUp(self):
        self.order_attr={'name': 'proda', 'description': ''}
        self.order = Order.objects.create(**self.order_attr)

        self.prod_attr={'name': 'prod1', 'price': 22.33}
        self.product = Product.objects.create(**self.prod_attr)

        self.order.products.add(self.product)

        self.serializer = OrderSerializer(instance=self.order)
        self.serializer_prod = ProductSerializer(instance=self.product)

    def test_string_record_order(self):
        '''Verifica stringa testo voce record modello Order'''
        data = self.serializer.data
        # print('\n\n\n###SERIAL- ORDER')
        # print(data)
        serial_string='%s - %s'%(data['name'],data['date'])
        self.assertEquals(self.order.__str__(), serial_string)

    def test_string_record_product(self):
        '''Verifica stringa testo voce record modello Product'''
        data = self.serializer_prod.data
        # print('\n\n\n###SERIAL PRODUCT')
        # print(data)
        serial_string='%s - %s'%(data['name'],data['price'])
        self.assertEquals(self.product.__str__(), serial_string)