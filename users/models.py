from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class person(AbstractBaseUser):
    name = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)

    USERNAME_FIELD = 'email'
    def __str__(self) -> str:
        return f'{self.name} {self.lastname}' 

class roles(models.Model):
    personName = models.ForeignKey(person, on_delete=models.CASCADE)
    rolename = models.CharField(max_length=50, blank=False)

    def __str__(self) -> str:
        return f'{self.personName} {self.rolename}'


