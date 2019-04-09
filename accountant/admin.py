from django.contrib import admin

from .models import Accountant

# Register your models here.
@admin.register(Accountant)
class AccountantAdmin(admin.ModelAdmin):
    list_display= ('pk','user_name','user_phone','is_accountant')
