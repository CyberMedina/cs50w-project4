from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User



class BaseLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adress_input = models.CharField(max_length=255, blank=False)
    direction_Name = models.CharField(max_length=15, blank=False)
    house_Number = models.CharField(max_length=50, blank=True)
    telephone_Number = models.CharField(max_length=15, blank=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.adress_input

class StaffLocation(BaseLocation):
    pass

class NoStaffLocation(BaseLocation):
    latitude = models.CharField(max_length=50, blank=False)
    longitude = models.CharField(max_length=50, blank= False)
    delivery_Instructions = models.CharField(max_length=255, blank=False)
    pass


    





    



