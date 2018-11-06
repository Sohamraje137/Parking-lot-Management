from django.db import models

# Create your models here.

class Employee(models.Model):
    user_name = models.CharField(u'user_name',default='abc',max_length = 20)
    user_first_name = models.CharField(u'Enter first name',max_length=15,default='Chaman')
    user_last_name = models.CharField(u'Enter first name',max_length=15,default='Chaman')
    user_phone =  models.CharField(u'cellphone number',max_length=10,default='')
    user_site_address =  models.CharField(u'Site Address',max_length=10,default='not assigned')


    def __str__(self):
        return u'%s' % self.user_name
    
    class Meta:
        verbose_name = 'Employee Data  '
        verbose_name_plural = ' Employee Data'
