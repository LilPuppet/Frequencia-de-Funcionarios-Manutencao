from django.test import TestCase

from rest_framework.test import APIClient
from django.test import TestCase

from django.contrib.auth.models import User


class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='lavinia', password='eusoufoda')
        response = self.client.post('/login/', {'username': 'lavinia', 'password': 'eusoufoda'})
        self.token = response.data['token']

    def test_usuarios(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
