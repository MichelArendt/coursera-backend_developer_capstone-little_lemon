from django.test import TestCase

from datetime import datetime, date

from restaurant import models

class MenuTest(TestCase):
    def test_get_item(self):
        item = models.Menu.objects.create(title='Ice Cream', price=80, inventory=100)

        self.assertEqual(str(item), 'Ice Cream : 80')

class BookingTest(TestCase):
    def test_get_item(self):
        booking = models.Booking.objects.create(name='John', nbr_of_guests=2, date=date.today(), time=datetime.now().time())

        print(str(booking))

        self.assertEqual(str(booking), 'John')