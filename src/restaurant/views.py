from django.shortcuts import render
from django.urls import get_resolver, get_urlconf, URLResolver, URLPattern
from django.urls.exceptions import NoReverseMatch

# from django_filters.rest_framework import DjangoFilterBackendpython
from django_filters import rest_framework as django_filters

from rest_framework import filters, generics, permissions
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . import models
from . import serializers

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
    return render(request, 'index.html', {})

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
    search_fields = ['name', 'nbr_of_guests', 'booking_date']
    ordering_fields = ['name', 'nbr_of_guests', 'booking_date']

    def get_permissions(self):
        if self.request.method == 'GET':
            return []

        return [permissions.IsAdminUser()]

# get, put, patch and delete
class SingleMBookingView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BookingSerializer
    queryset = models.Booking.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return []

        return [permissions.IsAdminUser()]

# class BookingViewSet(viewsets.ModelViewSet):
#     queryset = models.Booking.objects.all()
#     serializer_class = serializers.BookingSerializer
#     permission_classes = [permissions.IsAuthenticated]