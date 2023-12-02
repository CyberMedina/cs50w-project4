from django.utils import timezone
from django.db import models
from shop.models import Producto

# Create your models here.


class DeliveryInformation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    exact_address = models.TextField()
    house_number = models.CharField(max_length=50, blank=True)
    delivery_instructions = models.TextField()
    phone_number = models.CharField(max_length=15)

class Order(models.Model):
    delivery_info = models.ForeignKey(DeliveryInformation, on_delete=models.CASCADE)
    products = models.ManyToManyField(Producto)
    order_date = models.DateTimeField(default=timezone.now)
