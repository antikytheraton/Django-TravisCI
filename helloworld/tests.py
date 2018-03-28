from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


# Create your tests here.
class FirstTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.a = 1
        self.b = 2
        self.json_data = {'title': 'new idea'}

    def test_suma(self):
        self.assertEqual(self.a + self.b, 3)

    def test_post_response(self):
        response = self.client.post('/', self.json_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.json_data)

    def test_get_response(self):
        response = self.client.get('/')
        self.assertEqual(response.content, b'Hello World Travis setup!')
        