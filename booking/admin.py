from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'guests', 'day', 'time', 'customer', 'comment')


admin.site.register(Booking, BookingAdmin)
