from django.contrib import admin

# Register your models here.
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('pk','user_name','user_first_name','user_last_name','user_phone','user_site_address')


