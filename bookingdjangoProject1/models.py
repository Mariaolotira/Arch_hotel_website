from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    email = models.EmailField(max_length=50, blank=True, null=False)
    clients_quantity = models.IntegerField(blank=True, null=False)
    residence = models.CharField(max_length=50, blank=True, null=False, default="")
    phone = models.IntegerField(blank=True, null=False)
    stay_duration = models.IntegerField(blank=True, null=False, default='7')


def __str__(self):
    return self.name
