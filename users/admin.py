from django.contrib import admin

# Register your models here.
from .models import UserInfo
# Register your models here.

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('pk','user_name','user_phone','car_number','car_booking_status','car_site_address',
    'car_slot_no','admin_bit','car_type',)
    # exclude = ('user_name','car_number')


#     car_site_address = models.CharField(u'Site Number',max_length=20,null=True)
#    car_slot_no = models.CharField(u'Slot Number',max_length=20,null=True)

# 