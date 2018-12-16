from django.db import models
from django.conf import settings

# Create your models here.
from users.models import UserInfo
# Create your models here.
from carposition.models import Site,Positions


class Tariffs(models.Model):
    # user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    # user_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    user_name = models.CharField(u'user_name',default='abc',max_length = 20)
    car_number = models.CharField(u'Plate Number',max_length=20)
    start_time = models.DateTimeField(u'In-Time',null=True)
    end_time = models.DateTimeField(u'Out-Time',null=True)
    parking_time = models.FloatField(verbose_name='Parking time',default=0.0,editable=False,unique=False)
    parking_money = models.FloatField(verbose_name=u'Bill Amount',default=0.0,editable=False)
    TICKET_TYPE_CHOICES=(('Hour',u'Hour ticket'),    )
    ticket_type = models.CharField(u'Billing type',max_length=20,default='hour',choices=TICKET_TYPE_CHOICES,unique=False)
    per_hour_money = models.FloatField(verbose_name=u'Parking fees',default=0.0,editable=True)
    site_address= models.CharField(u'Site Address',max_length=20,default='Not Parked')
    postion_no= models.CharField(u'Parking Site Number',max_length=20,default='Not Parked')
    def __str__(self):
        return u'%s' % self.user_name
    
    class Meta:
        verbose_name = 'Tariffs Center'
        verbose_name_plural = 'Tariffs center'

class Tickets(models.Model):
    TICKET_TYPE_CHOICES=(('Hour',u'Hour ticket'),)
    ticket_type = models.CharField(u'Billing type',max_length=20,choices=TICKET_TYPE_CHOICES ,unique=False)
    per_hour_money = models.FloatField(verbose_name=u'Hourly parking fee',default=10.0,editable=True)
    
    class Meta:
        verbose_name = 'Tickets'
        verbose_name_plural = 'Tickets'


class Rates(models.Model):
    site_add= models.ForeignKey(Site, on_delete=models.CASCADE)

    # site_add =models.CharField(u'Site Address',default='',max_length = 20)
    pay_per_time= models.FloatField(u'Pay charges', default='40.00')
    def __str__(self):
        return u'%s' % self.site_add  
   
    class Meta:
        verbose_name = 'Rates'
        verbose_name_plural = 'Rates'