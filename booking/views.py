from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Booking
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib import messages



#class HomePage(generic.ListView):
#    model = Booking
#    template_name = 'index.html'

 
# View to make a reservation
class MakeBooking(generic.CreateView, LoginRequiredMixin):
    # specify the model for create view
    model = Booking
    template_name = 'index.html'
    # specify the fields to be displayed
    fields = ['guests', 'day', 'time', 'comment']
    
    def form_valid(self, form):
        # Connect the booking to the logged-in user
        form.instance.customer = self.request.user
        # Set a custom flag in the session to indicate successful confirmation
        self.request.session['booking_success'] = True

        # Call the parent class's form_valid method to save the booking
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the booking details page for the newly created booking
        return reverse('booking_details')


# View to display booking details
class BookingDetails(generic.ListView, LoginRequiredMixin):
    model = Booking
    template_name = 'booking_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        success_message = None

        # Check if the custom flag exists in the session
        if self.request.session.get('booking_success'):
            success_message = 'Your booking has been confirmed.'
            # Clear the custom flag
            del self.request.session['booking_success']

        context['success_message'] = success_message
        return context

    def get_queryset(self):
        return Booking.objects.filter(customer=self.request.user).order_by('day', 'time')

# View to delete bookings
class DeleteBooking(generic.DeleteView):
    model = Booking
    success_url = "/"

    template_name = "delete_booking.html"

class UpdateBooking(generic.UpdateView):
    model = Booking
    template_name = "update_booking.html"
    # specify the fields to be displayed
    fields = ['guests', 'day', 'time', 'comment']
    
    success_url = "/booking_details"



