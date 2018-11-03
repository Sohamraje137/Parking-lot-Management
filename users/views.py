from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from carposition.models import Positions
from users.models import UserInfo
from users.forms import LoginForm, RegForm, UserDetailForm

#from carposition.models import CarPosition

# Create your views here.

def home(request):
    car_positions =Positions.objects.filter(position_status=True)
    context = {}
    context['car_pos_num'] = car_positions.count()
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

def user_detail(request):
    if request.method =='POST':
        user_form = UserDetailForm(request.POST)
        if user_form.is_valid() and (request.user is not None):
            # Add user information

            user_info = UserInfo()
            user_info.user_name = request.user.username
            user_info.user_phone = user_form.cleaned_data['user_phone']
            user_info.car_number = user_form.cleaned_data['car_number']
            user_info.car_type = user_form.cleaned_data['car_type']
            user_info.car_color = user_form.cleaned_data['car_color']
            user_info.car_kind = user_form.cleaned_data['car_kind']
            user_info.save()
        return redirect(request.GET.get('from', reverse('home')))
    else:
        user_form = UserDetailForm()
    context = {}
    context['user_form'] = user_form
    return render(request,'user_detail.html',context)
