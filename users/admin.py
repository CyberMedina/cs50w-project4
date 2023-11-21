from django.contrib import admin
from .models import person, roles

# Register your models here.
admin.site.register(person)
admin.site.register(roles)
