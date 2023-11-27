from django.contrib import admin
from django.contrib.auth.models import User
from .models import StaffLocation, NoStaffLocation, CustomUser

class StaffLocationAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = CustomUser.objects.filter(is_staff=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class NoStaffLocationAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = CustomUser.objects.filter(is_staff=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
admin.site.register(CustomUser)
admin.site.register(NoStaffLocation, NoStaffLocationAdmin)
admin.site.register(StaffLocation, StaffLocationAdmin)

