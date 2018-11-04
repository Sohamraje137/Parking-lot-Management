from django.contrib import admin

# Register your models here.
from .models import UserInfo
# Register your models here.

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('pk','user_first_name','user_name','user_phone','car_number','car_booking_status','car_type','car_color','car_comapany')
    # exclude = ('user_name','car_number')
