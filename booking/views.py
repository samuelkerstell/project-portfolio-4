from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Booking
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError
from datetime import date

# View for home page
class HomePage(generic.TemplateView):
    template_name = 'index.html'


# View for menu page
class MenuPage(generic.TemplateView):
    template_name = 'menu.html'

 
# Code inspired from this https://www.geeksforgeeks.org/createview-class-based-views-django/?ref=lbp
class MakeBooking(generic.CreateView, LoginRequiredMixin):
    model = Booking
    template_name = 'booking_form.html'
    fields = ['guests', 'time', 'day', 'comment']
    
    def form_valid(self, form):
        # code altered from https://stackoverflow.com/questions/70671189/avoid-booking-past-dates-with-django
        start_date = form.cleaned_data.get('day')
        if start_date < date.today():
            messages.error(self.request, 'Booking date cannot be in the past.')
            return self.form_invalid(form)
    
        form.instance.customer = self.request.user
        self.request.session['booking_success'] = True

        try:
            return super().form_valid(form)
        except IntegrityError:
            # shows error message
            messages.error(self.request, 'You already have a booking for this time.')
            return self.form_invalid(form)

    def get_success_url(self):
        # Redirects to the booking details page for the newly created booking
        return reverse('booking_details')


# View to display booking details
# Code inspired from this https://www.geeksforgeeks.org/listview-class-based-views-django/
class BookingDetails(generic.ListView, LoginRequiredMixin):
    model = Booking
    template_name = 'booking_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        success_message = None

        if self.request.session.get('booking_success'):
            success_message = 'Your booking has been confirmed.'
            del self.request.session['booking_success']

        context['success_message'] = success_message
        return context

    def get_queryset(self):
        return Booking.objects.filter(customer=self.request.user).order_by('day', 'time')


# View to delete bookings
class DeleteBooking(generic.DeleteView, LoginRequiredMixin):
    model = Booking
    success_url = "/"

    template_name = "delete_booking.html"

    def get_queryset(self):
        return get_object_or_404(Booking, pk=self.kwargs['pk'], customer=self.request.user)


# View to update existing booking
# Code inspired from this https://www.geeksforgeeks.org/updateview-class-based-views-django/
class UpdateBooking(generic.UpdateView, LoginRequiredMixin):
    model = Booking
    template_name = "update_booking.html"
    fields = ['guests', 'time', 'day', 'comment']
    success_url = "/booking_details"

    def get_object(self):
        #return Booking.objects.filter(pk=self.kwargs['pk'], customer=self.request.user)
        return get_object_or_404(Booking, pk=self.kwargs['pk'], customer=self.request.user)


# Code taken from https://stackoverflow.com/questions/17662928/django-creating-a-custom-500-404-error-page
def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)
