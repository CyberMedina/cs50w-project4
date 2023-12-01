from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, AbstractUser


class CustomUser(AbstractUser):
    is_first_time_Google = models.BooleanField(default=False)






class BaseLocation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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


def get_google_maps_url(lat, lon):
    base_url = "https://www.google.com/maps/search/?api=1&query="
    return base_url + str(lat) + "," + str(lon)


class NoStaffLocation(BaseLocation):
    latitude = models.CharField(max_length=50, blank=False)
    longitude = models.CharField(max_length=50, blank= False)
    delivery_Instructions = models.CharField(max_length=255, blank=False)

    def get_google_maps_url(self):
        base_url = "https://www.google.com/maps/search/?api=1&query="
        return base_url + str(self.latitude) + "," + str(self.longitude)


    
    def get_full_adress(self):
        googlemaps_url = get_google_maps_url(self.latitude, self.longitude)
        return f'{self.direction_Name}, {self.adress_input}, {self.house_Number}, {self.delivery_Instructions}, {self.telephone_Number}, {googlemaps_url}'


    pass


    





    



