from django.shortcuts import render
from django.http import HttpResponse
from .models import Site,Positions
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from users.models import UserInfo
from tariff.models import Tariffs,Tickets
import time
import random
from djqscsv import render_to_csv_response
from django.contrib.auth.models import User

# Create your views here.

def car_site_index(request):#,site_num):
    # site_no = get_object_or_404(Site, site_num=site_num)
    positions_list = Site.objects.filter()
    context = {}
    context['positions_list']=positions_list
    return render(request,'car_site_index.html',context)

def site_position_book(request,site_no):
    positions_list = Site.objects.filter(site_no=site_no)
    context = {
        'site_no':site_no
    }
    context['positions_list']=positions_list
    return render(request,'car_posi_index.html',context)



def download_positions(request):
    qs = Site.objects.all()    
    return render_to_csv_response(qs,filename=u'slots.csv')

# def order_position1(request,site_no,posi_num):
#     # Change parking space inventory information
#     order_info = Site.objects.filter(site_no=site_no)
#     position_booking = Positions.objects.filter(site_no=site_no)
#     car_order = Site()
#     car_order.pk = site_no
#     car_order.site_no= site_no
#     car_order.position_num = order_info.position_num

#     car_order.position_status = False
#     car_order.save()

#     # Increase ticketing information
#     user_info = UserInfo.objects.get(user_name=request.user.username) #Get user information
#     ticket = Tickets.objects.order_by('-per_hour_money')
#     tariff = Tariffs()
#     tariff.user_name = request.user.username
#     tariff.car_number = user_info.car_number
#     tariff.ticket_type = 'Hour'
#     pt = random.choice((0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5))
#     tariff.parking_time = pt #
#     tariff.parking_money = pt * ticket[0].per_hour_money
#     tariff.save()    
#     # qs = Tariffs.objects.all()
#     # return render_to_csv_response(qs,filename=u'tariffs.csv')
#     return HttpResponse('Dear{0}Already reserved{1}'.format(request.user.username,order_info.position_num))


def order_position(request,site_no,posi_num):
    # site_object = Site.objects.get(site_no=site_no)
    # # position_object =Positions.objects.filter(position_num= posi_num)
    # # position_object.position_status =False 
    # # selected_choice = site_object.positions_set.get(pk=request.POST['positions'])
    # # selected_choice.position_status=False
    
    # print(site_object.site_address)
    # site_new_object= Site()
    # site_new_object.site_no = site_no
    # site_new_object.pay_per_time= site_object.pay_per_time
    # site_new_object.max_capacity = site_object.max_capacity
    # site_new_object.site_address= site_object.site_address

    # selected_option = site_new_object.positions_set.get(pk=site_no)
    # selected_option.position_status=False

    # site_new_object.save()
    position_object=Positions.objects.get(site_no=site_no, position_num = posi_num)
    position_object.position_status = False
    position_object.save()
    #selected_choice.save()
      #   position_object.save()
        # Increase ticketing information 
    
    user_info = User.objects.get(username=request.user) #Get user information
    
    ticket = Tickets.objects.order_by('-per_hour_money')
    tariff = Tariffs()
    tariff.user_name = request.user
    UserInfoInstance = UserInfo.objects.get(user_name=user_info)
    print(UserInfoInstance.car_number)
    tariff.car_number = UserInfoInstance.car_number
    tariff.ticket_type = 'Hour'
    pt = random.choice((0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5))
    tariff.parking_time = pt #
    tariff.parking_money = pt * ticket[0].per_hour_money
    tariff.save()    
    return HttpResponse('Dear{0} parking slot is reserved for you  {1}'.format(request.user.username,position_object.position_num))
