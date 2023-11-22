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
    
class location(models.Model):
    person = models.ForeignKey(person, on_delete=models.CASCADE)
    adressinput = models.CharField(max_length=255, blank=False)
    latitude = models.CharField(max_length=50, blank=False)
    longitude = models.CharField(max_length=50, blank= False)
    houseNumber = models.CharField(max_length=50, blank=True)
    deliveryInstructions = models.CharField(max_length=255, blank=False)
    directionName = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return f'{self.directionName} {self.adressinput}'

class phoneNumbers(models.Model):
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    telephoneNumber = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return f'{self.location.person.name} {self.location.person.lastname} {self.location.directionName} {self.telephoneNumber}'

class rol(models.Model):
    rolename = models.CharField(max_length=50, blank=False)

    def __str__(self) -> str:
        return f'{self.rolename}'
    

class user(models.Model):
    person = models.ForeignKey(person, on_delete=models.CASCADE)
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    number = models.ForeignKey(phoneNumbers, on_delete=models.CASCADE)
    rol = models.ManyToManyField(rol, blank=True, related_name="users")

    def __str__(self):
        roles = self.rol.all()
        role_names = [role.rolename for role in roles]
        return f'{self.person.name} {self.person.lastname} Roles: {", ".join(role_names)}'



    



