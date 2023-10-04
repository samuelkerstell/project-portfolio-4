from . import views
from django.urls import path

urlpatterns = [
    #path('', views.HomePage.as_view(), name='home'),
    path('', views.MakeBooking.as_view(), name='home'),
    path('booking_details/', views.BookingDetails.as_view(), name='booking_details'),
    path('booking_error/', views.BookingError.as_view(), name='booking_error'),
    path('<pk>/delete/', views.DeleteBooking.as_view(), name='delete_booking'),
    path('<pk>/update', views.UpdateBooking.as_view(), name='update_booking'),
]


# Code taken from https://stackoverflow.com/questions/17662928/django-creating-a-custom-500-404-error-page
handler404 = 'booking.views.handler404'
handler500 = 'booking.views.handler500'