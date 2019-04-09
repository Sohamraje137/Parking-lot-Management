from django.db import models

# Create your models here.
class Accountant(models.Model):
    # userforeignkey = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(u'username',max_length=15,default='')
    user_phone =  models.CharField(u'cellphone number',max_length=10,default='')
    is_accountant =  models.BooleanField('Accountant Bit',default=False)

    def __str__(self):
        return u'%s' % self.user_name
    class Meta:        
        verbose_name = 'Accountant Info'
        verbose_name_plural = 'Accountant Info'