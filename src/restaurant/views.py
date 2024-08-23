from django.shortcuts import render, redirect
from django.urls import get_resolver, get_urlconf, URLResolver, URLPattern
from django.urls.exceptions import NoReverseMatch
import django
from django_filters import rest_framework as django_filters

from rest_framework import filters, generics, permissions
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from datetime import datetime, timedelta, date

from . import models, serializers, forms

class APIRootView(APIView):
    def get(self, request, format=None):
        # Initial API URLs, including your custom views
        api_urls = {
            'menu-list': reverse('menu-list', request=request, format=format),
            'menu-item-view': reverse('menu-item-view', kwargs={'pk': 1}, request=request, format=format),
            'booking-list': reverse('booking-list', request=request, format=format),
            'booking-item-view': reverse('booking-item-view', kwargs={'pk': 1}, request=request, format=format),
        }

        # Djoser URLs as a nested dictionary
        djoser_urls = {}

        # Helper function to recursively extract URL patterns
        def extract_urls(resolver, prefix=''):
            for pattern in resolver.url_patterns:
                if isinstance(pattern, URLResolver):
                    # Recursively resolve nested resolvers
                    extract_urls(pattern, prefix=prefix + pattern.pattern.regex.pattern)
                elif isinstance(pattern, URLPattern):
                    # Use the pattern's regex to check if it starts with 'api/auth/'
                    full_pattern = prefix + pattern.pattern.regex.pattern
                    try:
                        if 'api/auth/' in full_pattern:  # Adjust to match the correct prefix
                            djoser_urls[pattern.name] = reverse(pattern.name, request=request, format=format)
                            print('Added:', pattern.name)
                        else:
                            print('Not added:', full_pattern)
                    except NoReverseMatch:
                        print('No reverse match:', full_pattern)
                        pass

        # Get the root resolver and extract URLs
        resolver = get_resolver()
        extract_urls(resolver)
        api_urls['auth_endpoints'] = djoser_urls

        return Response(api_urls)

def index(request):
    return render(request, 'home.html', {})

def menu(request):
    menu_items = models.Menu.objects.all().order_by('title')

    return render(request, 'menu.html', { 'menu_items': menu_items})

def booking(request):
    # Initialize form for both GET and POST requests
    form = forms.BookingForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # Save the form data to the database
        form.save()

        # Redirect to the same page to reset the form
        return redirect('booking')

    # Set the date field's widget type to 'date' and set the minimum date to today
    form.fields['date'].widget = django.forms.DateInput(attrs={
        'type': 'date',
        'min': date.today().isoformat(),  # Set the minimum date to today's date
    })

    # Change the label of the 'nbr_of_guests' field
    form.fields['nbr_of_guests'].label = 'Number of Guests'

    # Add a placeholder to the 'nbr_of_guests' field
    form.fields['nbr_of_guests'].widget.attrs.update({'placeholder': 'Enter number of guests'})

    # Generate time slots in 30-minute increments from 11:00 to 23:00
    opening_time = datetime.strptime('11:00', '%H:%M').time()
    closing_time = datetime.strptime('23:00', '%H:%M').time()
    time_slots = []

    current_time = datetime.combine(date.today(), opening_time)
    end_time = datetime.combine(date.today(), closing_time)

    while current_time <= end_time:
        time_slots.append((current_time.strftime('%H:%M'), current_time.strftime('%I:%M %p')))
        current_time += timedelta(minutes=60)

    # Check for existing bookings for the selected date
    selected_date = form.data.get('date') or date.today()  # Use today's date if no date is selected
    booked_times = models.Booking.objects.filter(date=selected_date).values_list('time', flat=True)

    # Convert booked_times to strings in 'HH:MM' format for comparison
    booked_times = [bt.strftime('%H:%M') for bt in booked_times]

    # Mark booked times as disabled
    time_choices = []
    print('booked_times: ' + str(booked_times))
    for time_slot in time_slots:
        print('time_slot: ' + str(time_slot))
        if time_slot[0] in booked_times:
            print(1)
            time_choices.append((time_slot[0], f"{time_slot[1]} (Booked)"))
        else:
            print(2)
            time_choices.append((time_slot[0], time_slot[1]))

    print("Final time choices:", time_choices)

    form.fields['time'].choices = time_choices

    # Render the form with the correct time choices
    return render(request, 'booking.html', {'form': form})

# get and post
class MenuItemsView(generics.ListCreateAPIView):
    serializer_class = serializers.MenuSerializer
    queryset = models.Menu.objects.all()

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'price']
    ordering_fields = ['title', 'price']

    def get_permissions(self):
        if self.request.method == 'GET':
            return []

        return [permissions.IsAdminUser()]

# get, put, patch and delete
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MenuSerializer
    queryset = models.Menu.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return []

        return [permissions.IsAdminUser()]

# get and post
class BookingsView(generics.ListCreateAPIView):
    serializer_class = serializers.BookingSerializer
    queryset = models.Booking.objects.all()

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'nbr_of_guests', 'date','time']
    ordering_fields = ['name', 'nbr_of_guests', 'date','time']

    def get_permissions(self):
        if self.request.method == 'POST':
            return []

        return [permissions.IsAdminUser()]

# get, put, patch and delete
class SingleMBookingView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BookingSerializer
    queryset = models.Booking.objects.all()

    def get_permissions(self):
        return [permissions.IsAdminUser()]