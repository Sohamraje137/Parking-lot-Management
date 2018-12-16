from django.db import models
from django.contrib.auth.models import User

# Create your models here
class UserInfo(models.Model):
    # userforeignkey = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(u'username',max_length=15,default='')
    user_phone =  models.CharField(u'cellphone number',max_length=10,default='')
    # user_first_name = models.CharField(u'Enter first name',max_length=15,default='Chaman')
    car_number = models.CharField(u'Car number plate',max_length=10,default='')
    car_type = models.CharField(u'Model',max_length=11,default='')
    # car_color = models.CharField(u'Car color',max_length=8,default='')
    # car_comapany = models.CharField(u'Car company',max_length=8,default='')
    car_booking_status=  models.BooleanField('Booking status',default=False)
    car_site_address = models.CharField(u'Site Number',max_length=20,null=True)
    car_slot_no = models.CharField(u'Slot Number',max_length=20,null=True)
    admin_bit=  models.BooleanField('Admin Bit',default=False)

    def __str__(self):
        return u'%s' % self.car_number
    class Meta:        
        verbose_name = 'User Info'
        verbose_name_plural = 'User Info'