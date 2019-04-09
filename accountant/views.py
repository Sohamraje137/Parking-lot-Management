from django.shortcuts import render
from django.http import HttpResponse
from carposition.models import Site,Positions
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
import time
from datetime import datetime, date, time, timedelta
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

def accounts_index(request):#,site_num):
    if not request.user.is_accountant:
        return redirect('/users/home')
    # site_no = get_object_or_404(Site, site_num=site_num)
    if not request.user.is_authenticated:
        return redirect('/users/home')
    # for rate in rates:
    #     print(rate.pay_per_time)
    tariffobject= Tariffs.objects.filter() #    rates= Rates.objects.filter()
    totalamount = 0

    for i in tariffobject:
        totalamount+= i.parking_money
    print(totalamount)
    context = {
        'totalamount':totalamount,
        'tariffobject' : tariffobject,
    }
    return render(request,'accounts_index.html',context)
