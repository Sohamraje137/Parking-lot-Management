from django.contrib import admin

# Register your models here.
from .models import Sitemanager


@admin.register(Sitemanager)
class SitemanagerAdmin(admin.ModelAdmin):
    list_display = ('pk','user_name', 'user_phone' , 'site_no' , 'is_manager' )
