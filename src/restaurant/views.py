from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets, permissions

from . import models
from . import serializers

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# get and post
class MenuItemsView(generics.ListCreateAPIView):
    serializer_class = serializers.MenuSerializer
    queryset = models.Menu.objects.all()

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return []

    #     return [IsAdminUser()]

# get, put, patch and delete
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MenuSerializer
    queryset = models.Menu.objects.all()

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return []

    #     return [IsAdminUser()]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.IsAuthenticated]