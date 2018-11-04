from django.db import models

# Create your models here.
class Site(models.Model):
    site_no= models.IntegerField(u'site number',default=0,primary_key=True)
    site_address=models.CharField(max_length=200,default='Mangalore')
    pay_per_time=models.FloatField(u'cost',default='15.0')
    max_capacity=models.IntegerField(u'Capacity',default=0)

    def __str__(self):
      return self.site_address


class Positions(models.Model):
    site_no= models.ForeignKey(Site, on_delete=models.CASCADE)
    position_num = models.CharField('Parking number',max_length=20,default='')
    position_status = models.BooleanField('Parking status [default is unoccupied]',default=True)
    def __str__(self):
      return self.position_num

    class Meta:
        verbose_name = 'Positions'
        verbose_name_plural = 'Positions'
    
