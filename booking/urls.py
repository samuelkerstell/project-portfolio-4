from . import views
from django.urls import path

urlpatterns = [
    #path('', views.HomePage.as_view(), name='home'),
    path('', views.MakeBooking.as_view(), name='home'),
    path('booking_details/', views.BookingDetails.as_view(), name='booking_details'),
]