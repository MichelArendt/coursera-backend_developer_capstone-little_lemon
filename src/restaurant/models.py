from django.db import models
from datetime import date, datetime

def current_time():
    return datetime.now().time()

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    name = models.CharField(max_length=255)
    nbr_of_guests = models.IntegerField()
    date = models.DateField(default=date.today)  # Default to today's date
    time = models.TimeField(default=current_time)  # Default to current time

    def __str__(self):
        return self.name