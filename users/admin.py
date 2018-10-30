from django.contrib import admin

# Register your models here.
from .models import UserInfo
# Register your models here.

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('pk','user_name','car_number','car_type','car_color')
    # exclude = ('user_name','car_number',)
