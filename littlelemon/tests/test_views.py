from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from django.contrib.auth.models import User
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        Menu.objects.create(
            title="Pizza",
            price=20,
            inventory=10
        )

        Menu.objects.create(
            title="Burger",
            price=15,
            inventory=5
        )

    def test_getall(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get('/restaurant/menu/')

        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)