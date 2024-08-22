from django.urls import path

from . import views

urlpatterns = [
    path('', views.APIRootView.as_view(), name='api-root'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-item-view'),
    path('booking/', views.BookingsView.as_view(), name='booking-list'),
    path('booking/<int:pk>/', views.SingleMBookingView.as_view(), name='booking-item-view'),
]