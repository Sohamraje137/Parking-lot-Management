from django.db import models

# Create your models here.
class Sitemanager(models.Model):
    # userforeignkey = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(u'username',max_length=35,default='')
    user_phone =  models.CharField(u'cellphone number',max_length=10,default='')
    site_no= models.IntegerField(u'site number',default=0,primary_key=True)

    is_manager =  models.BooleanField('Site Manager Bit',default=False)

    def __str__(self):
        return u'%s' % self.user_name
    class Meta:        
        verbose_name = 'Site Manager Info'
        verbose_name_plural = 'Site Manager Info'