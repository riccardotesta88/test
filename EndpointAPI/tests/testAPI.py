from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory,APITestCase, URLPatternsTestCase, force_authenticate
from rest_framework import status
from rest_framework.test import APIClient
from requests.auth import HTTPBasicAuth
import json
from rest_framework.authtoken.models import Token

class OrderTests(APITestCase):

    def setUp(self):
        username='operatore'
        password='operatore'

        self.factory= APIRequestFactory()

        #Accesso con credenziali
        self.client = APIClient()

        # Autenticazione base
        self.client.login(username=username, password=password)
        self.client.auth = HTTPBasicAuth('operatore', 'operatore')
        # self.client.headers.update({'x-test': 'true'})

        #Autorizzazione con token
        # token = Token.objects.get(user=username)
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)



    def test_full_list(self):
        '''Lista ordini presenti '''
        response=self.client.get('/api/orders/',{}, format='json')
        assert response.status_code==status.HTTP_200_OK
        parsed=json.decode(response.data)
        #print(parsed)
        self.assertEqual(len(parsed), 9)

    def test_detail_order(self):
        '''Accesso alle API con autenticazione base '''
        response=self.client.get('/api/orders/1/', {}, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        parsed=response
        print(parsed)

        self.assertEqual(parsed['name'],'proda')
        self.assertEqual(parsed['description'],'')
        self.assertEqual(parsed['date'],'2024-06-23 12:05:32')
        self.assertEqual(parsed['products'],[1])


    def test_order_update(self):
        '''Accesso alle API con autenticazione base '''
        response=self.client.put('/api/orders/1/',{'name':'Frasso'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        parsed=json.decode(response.data)
        print(parsed)
        self.assertEqual(len(parsed),1)
        self.assertEqual(parsed['name'],'Frasso')

    def test_order_delete(self):
        '''Accesso alle API con autenticazione base '''
        response=self.client.delete('/api/orders/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response=self.client.get('/api/orders/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


