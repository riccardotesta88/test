from rest_framework.test import APITestCase, URLPatternsTestCase, force_authenticate
from rest_framework import status
from rest_framework.test import APIClient
from requests.auth import HTTPBasicAuth
import json

class OrderTests(APITestCase):

    def setUp(self):
        #Accesso con credenziali
        self.client = APIClient()
        # Autenticazione base
        self.client.login('operatore', 'operatore')
        self.client.auth = HTTPBasicAuth('operatore', 'operatore')
        self.client.headers.update({'x-test': 'true'})


    def full_list(self):
        '''Lista ordini presenti '''
        response=self.client.get('/api/orders/',{}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        parsed=json.decode(response.data)
        print(parsed)

        self.assertEqual(len(parsed), 9)

    def detail_order(self):
        '''Accesso alle API con autenticazione base '''
        response=self.client.get('/api/orders/1',{}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        parsed=json.decode(response.data)
        print(parsed)

        self.assertEqual(len(parsed),1)
        self.assertEqual(parsed['name'],'prova')
        self.assertEqual(parsed['description'],'casco')
        self.assertEqual(parsed['date'],'2024-06-17T07:35:14.538657Z')
        self.assertEqual(parsed['products'],[1])
