from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

time_options = (
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
    ("19:00", "19:00"),
    ("20:00", "20:00"),
)

GUEST_CAPACITY = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
)


class Booking(models.Model):
    guests = models.CharField(max_length=10, choices=GUEST_CAPACITY,
                              default="1")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=time_options,
                            default="09:00")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                                 blank=True)
    email = models.EmailField(default="")
    comment = models.TextField(max_length=40, blank=True)

    class Meta():
        unique_together = ['day', 'time', 'customer']

    def __str__(self):
        return f"Booking for {self.customer} at {self.day} {self.time}"
