from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from carposition.models import Positions
from users.models import UserInfo
from users.forms import LoginForm, RegForm, UserDetailForm
from django.conf import settings
from tariff.models import Tariffs
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
# import datetime
# import time
# from datetime import datetime, date, time, timedelta

from django.utils import timezone
import datetime
import time
from datetime import datetime, date, time, timedelta


@cache_control(no_cache=True, must_revalidate=True, no_store=True)


def home(request):
    # print("HI")

    car_positions =Positions.objects.filter(position_status=True)
    car_pos_num = car_positions.count()

    if request.user.is_authenticated and  not request.user.is_superuser :
        print(request.user)
        User_info = UserInfo.objects.get(user_name=request.user)
        print(User_info.car_booking_status)
        print(car_pos_num)
        context = {
        'User_info': User_info,
        'car_pos_num' : car_pos_num,
        }
    else:
        context = {
            'car_pos_num' : car_pos_num
    }
    print("Rendering home")   
    return render(request,'home.html',context)

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        login_form = LoginForm()
    context = {}
    context['login_form'] = login_form
    return render(request, 'login.html', context)

def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # Create user
           
            user = User.objects.create_user(username, email, password)
            print(user.username)
            user.save()
            # Login user

            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('user_detail')))
    else:
        reg_form = RegForm()
    context = {}
    context['reg_form'] = reg_form
    return render(request, 'register.html', context)

@login_required
def user_detail(request):
    if request.method =='POST':
        user_form = UserDetailForm(request.POST)
        if user_form.is_valid() and (request.user is not None):
            # Add user information
            # print("Hello")
            user_info = UserInfo()
            # print("Hi")
            user_info.user_name = request.user.username
            # user_info.user_name = user_form.cleaned_data['user_name']
            # user_info.user_first_name= user_form.cleaned_data['user_first_name']
            user_info.user_phone = user_form.cleaned_data['user_phone']
            user_info.car_number = user_form.cleaned_data['car_number']
            user_info.car_type = user_form.cleaned_data['car_type']
            # user_info.car_color = user_form.cleaned_data['car_color']
            # user_info.car_kind = user_form.cleaned_data['car_kind']
            user_info.save()
        return redirect(request.GET.get('from', reverse('home')))
    else:
        user_form = UserDetailForm()
    context = {}
    context['user_form'] = user_form
    return render(request,'user_detail.html',context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

def Checkoutuser(request):
    UserInfolist = UserInfo.objects.values()

    # print(UserInfolist)
    context={
        'UserInfolist':UserInfolist
    }

    return render(request,'Checkoutuser.html',context)


def emptyslot(request,username):
    print(username)
    UserInfoobject = UserInfo.objects.get(user_name= username)
    UserInfoobject.admin_bit= True
    UserInfoobject.car_booking_status=False
    Tariffobject= Tariffs.objects.get(user_name=username)
    Tariffobject.end_time = datetime.now()

    print(datetime.now())
    print(Tariffobject.start_time)
    print(Tariffobject.end_time)
    Positionobject= Positions.objects.get(position_num =Tariffobject.postion_no)
    Positionobject.position_status=True
    '''    if(hoursspent>1):
        query.parking_money=hoursspent*query.per_hour_money
    else:
        query.parking_money=query.per_hour_money
    
    query.parking_time = hoursspent
    query.save()'''
    print(Tariffobject.start_time.hour)
    print(Tariffobject.end_time.hour)
    st_sec = Tariffobject.start_time.second + Tariffobject.start_time.minute*60 + Tariffobject.start_time.hour*24*60
    et_sec = Tariffobject.end_time.second+ Tariffobject.end_time.minute*60 + Tariffobject.end_time.hour*24*60
    hoursspent = (et_sec-st_sec)
    print(hoursspent)
    hoursspent = hoursspent//3600
    print(st_sec)
    print(et_sec)
    print(hoursspent)
    if(hoursspent>1):
        # hoursspent=hoursspent*Tariffobject.per_hour_money
        Tariffobject.parking_money= hoursspent*Tariffobject.per_hour_money
    else:
        Tariffobject.parking_money=Tariffobject.per_hour_money
    print(hoursspent)
    Tariffobject.parking_time = hoursspent
    Positionobject.save()
    UserInfoobject.save()
    Tariffobject.save()
    context= {
        'tariffobject':Tariffobject,
    }
    return render(request,'emptyslot.html',context)