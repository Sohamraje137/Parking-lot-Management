from django.shortcuts import render
from django.http import HttpResponse
from .models import Site,Positions
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from users.models import UserInfo
from tariff.models import Tariffs,Tickets,Rates
import time
import random
from djqscsv import render_to_csv_response
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.conf import settings

# Create your views here.

def car_site_index(request):#,site_num):
    # site_no = get_object_or_404(Site, site_num=site_num)
    if not request.user.is_authenticated:
        return redirect('/users/home')
    rates= Rates.objects.filter()
    positions_list = Site.objects.filter()#(position_status=True)
    for rate in rates:
        print(rate.pay_per_time)
    zipped_data=zip(positions_list, rates)
    context = {
        'rates': rates,
        'positions_list':positions_list,
        'zipped_data':zipped_data
    }
    return render(request,'car_site_index.html',context)

def site_position_book(request,site_no):
    # status_list = Positions.objects.get(site_no=site_no)
    if not request.user.is_authenticated:
        return redirect('/users/home')
    positions_list = Site.objects.filter(site_no=site_no)# and status_list.site_no=site_no and status_list.position_status=True )
    # site_name= Site.objects.filter(site_no=site_no).site_address
    context = {
        'site_no':site_no,
        # 'site_name':site_name
    }

    print(positions_list)
    context['positions_list']=positions_list
    return render(request,'car_posi_index.html',context)



def download_positions(request):
    qs = Site.objects.all()    
    return render_to_csv_response(qs,filename=u'slots.csv')

def order_position(request,site_no,posi_num):
    if not request.user.is_authenticated:
        return redirect('/users/home')
    position_object=Positions.objects.get(site_no=site_no, position_num = posi_num)
    position_object.position_status = False
    position_object.save()

    user_info = User.objects.get(username=request.user) #Get user information
    ticket = Tickets.objects.order_by('-per_hour_money')
    tariff = Tariffs()
    tariff.user_name = request.user
    UserInfoInstance = UserInfo.objects.get(user_name=user_info)
    print(UserInfoInstance.car_number)
    UserInfoInstance.car_booking_status = True
    print(UserInfoInstance.car_booking_status)
    UserInfoInstance.save()
    tariff.car_number = UserInfoInstance.car_number
    tariff.ticket_type = 'Hour'
    pt = random.choice((0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5))
    tariff.parking_time = pt #
    tariff.parking_money = pt * ticket[0].per_hour_money
    tariff.save()    

    return render(request , 'bocked.html')
