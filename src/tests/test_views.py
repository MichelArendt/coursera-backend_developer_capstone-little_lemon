from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        # Create a few test instances of the Menu model
        Menu.objects.create(title='Ice Cream', price=80, inventory=100)
        Menu.objects.create(title='Pizza', price=150, inventory=50)
        Menu.objects.create(title='Burger', price=120, inventory=30)

        # Initialize the APIClient for testing
        self.client = APIClient()

    def test_getall(self):
        # Perform a GET request to retrieve all Menu objects
        response = self.client.get('/restaurant/menu/')  # Adjust the URL to match your actual endpoint

        # Get all Menu objects from the database
        menus = Menu.objects.all()

        # Serialize the data
        serializer = MenuSerializer(menus, many=True)

        # Assert that the serialized data matches the response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)