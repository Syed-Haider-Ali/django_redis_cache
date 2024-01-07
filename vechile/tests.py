from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Vechile, Make


class MakeAPIViewTest(APITestCase):
    fixtures = ['data/make_data.json']
    url = reverse('make_view')

    def test_create(self):
        data = {"name":"United"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.data['data']['count'], 7)    
        self.assertEqual(response.status_code, 200)    

    def test_get_params(self):
        response = self.client.get(self.url + "?id=1")
        self.assertEqual(response.data['data']['count'], 1)    
        self.assertEqual(response.status_code, 200)   


class VechileAPIViewTest(APITestCase):
    fixtures = ['data/make_data.json']
    url = reverse('vechile_view')

    def test_create(self):
        data = {
            "name":"Mehran",
            "make":8,
            "model":2009,
            "color":"White"
            }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)




        
           


        