from django.contrib import admin

# Register your models here.
from .models import Site,Positions


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('pk','site_no','site_address','pay_per_time','max_capacity')

@admin.register(Positions)
class PositionsAdmin(admin.ModelAdmin):
    list_display=('site_no','position_num','position_status')
