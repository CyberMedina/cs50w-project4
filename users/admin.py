from django.contrib import admin
from .models import person, rol, user, phoneNumbers, location

# Register your models here.
admin.site.register(person)
admin.site.register(location)
admin.site.register(phoneNumbers)
admin.site.register(rol)
admin.site.register(user)


