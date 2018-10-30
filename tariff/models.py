from django.db import models

# Create your models here.
from users.models import UserInfo
# Create your models here.

class Tariffs(models.Model):
    # user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    user_name = models.CharField(u'user_name',default='abc',max_length = 20)
    car_number = models.CharField(u'Plate Number',max_length=20)
    start_time = models.DateTimeField(u'In Time',auto_now_add=True)
    end_time = models.DateTimeField(u'Out-Time',auto_now=True)
    parking_time = models.FloatField(verbose_name='Parking time',default=0.0,editable=False,unique=False)
    parking_money = models.FloatField(verbose_name=u'parking fee',default=0.0,editable=False)
    TICKET_TYPE_CHOICES=(('Hour',u'Hour ticket'),    )
    ticket_type = models.CharField(u'Billing type',max_length=20,choices=TICKET_TYPE_CHOICES,unique=False)
    per_hour_money = models.FloatField(verbose_name=u'Hourly parking fees',default=100.0,editable=True)
    def __str__(self):
        return u'%s' % self.ticket_type
    
    class Meta:
        verbose_name = 'Ticket Center'
        verbose_name_plural = 'Ticket center'

class Tickets(models.Model):
    TICKET_TYPE_CHOICES=(('Hour',u'Hour ticket'),)
    ticket_type = models.CharField(u'Billing type',max_length=20,choices=TICKET_TYPE_CHOICES ,unique=False)
    per_hour_money = models.FloatField(verbose_name=u'Hourly parking fee',default=10.0,editable=True)
    
    class Meta:
        verbose_name = 'Charge type'
        verbose_name_plural = 'Charge type'