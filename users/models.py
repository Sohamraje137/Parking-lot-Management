from django.db import models

# Create your models here
class UserInfo(models.Model):
    user_name = models.CharField(u'username',max_length=15,default='')
    user_phone =  models.CharField(u'cellphone number',max_length=15,default='')
    car_number = models.CharField(u'Car number plate',max_length=10,default='')
    car_type = models.CharField(u'Model',max_length=11,default='')
    car_color = models.CharField(u'Car color',max_length=8,default='')
    car_comapany = models.CharField(u'car company',max_length=8,default='')

    def __str__(self):
        return u'%s' % self.car_number
    class Meta:        
        verbose_name = 'User Info'
        verbose_name_plural = 'User Info'