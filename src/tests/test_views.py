from django.test import TestCase

from datetime import datetime, date

from rest_framework.test import APIClient
from rest_framework import status

from restaurant import models
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        # Create a few test instances of the Menu model
        models.Menu.objects.create(title='Ice Cream', price=80, inventory=100)
        models.Menu.objects.create(title='Pizza', price=150, inventory=50)
        models.Menu.objects.create(title='Burger', price=120, inventory=30)

        # Initialize the APIClient for testing
        self.client = APIClient()

    def test_get_all(self):
        # Perform a GET request to retrieve all Menu objects
        response = self.client.get('/api/menu/')

        # Get all Menu objects from the database
        menus = models.Menu.objects.all()

        # Serialize the data
        serializer = MenuSerializer(menus, many=True)

        # Assert that the status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the serialized data matches the 'results' key in the response
        self.assertEqual(response.data['results'], serializer.data)

class BookingViewTest(TestCase):
    def setUp(self) -> None:
        models.Booking.objects.create(name='John', nbr_of_guests=2, date=date.today(), time=datetime.now().time())

        # Initialize the APIClient for testing
        self.client = APIClient()

    def test_get_all_anonymous(self):
        response = self.client.get('/api/booking/')

        # Assert that the status code is 401 Unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)