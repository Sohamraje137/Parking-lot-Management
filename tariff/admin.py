from django.contrib import admin

# Register your models here.
from .models import Tariffs,Tickets,Rates


@admin.register(Tickets)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('pk','ticket_type','per_hour_money')

@admin.register(Tariffs)
class TariffsAdmin(admin.ModelAdmin):
    list_display = ('pk','user_name','car_number','start_time','ticket_type','parking_time','parking_money')
    exclude = ('per_hour_money',)

@admin.register(Rates)
class RatesAdmin(admin.ModelAdmin):
    list_display=('pk','pay_per_time','site_add',)
