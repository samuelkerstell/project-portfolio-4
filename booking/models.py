from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

time_options = (
    ("09:00", "09:00"),
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
)

GUEST_CAPACITY = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
)


# Create your models here.
#class Customer(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    email = models.EmailField()

#    def __str__(self):
#        return self.user.get_full_name() if self.user.get_full_name() else self.user.username


class Booking(models.Model):
    guests = models.CharField(max_length=10, choices=GUEST_CAPACITY, default="1")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=time_options, default="09:00")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(default="")
    comment = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return f"Booking for {self.customer} at {self.day} {self.time}"
