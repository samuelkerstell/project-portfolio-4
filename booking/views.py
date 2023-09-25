from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Booking
from django.views import generic

# Create your views here.

class HomePage(generic.ListView):
    model = Booking
    template_name = 'index.html'


# View to display available tables
#def available_booking_times(request):
    
# View to make a reservation
class MakeBooking(Booking):
    model = Booking

# View to display booking details
#def booking_details(request, booking_id):