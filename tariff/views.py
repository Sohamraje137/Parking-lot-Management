
import csv
from djqscsv import render_to_csv_response
from django.shortcuts import render
from django.http import HttpResponse
from tariff.models import Tariffs,Rates
from users.models import UserInfo
from django.conf import settings
from django.shortcuts import redirect
from django.utils import timezone
# Create your views here.
import datetime
import time
from datetime import datetime, date, time, timedelta

def index(request):
    return HttpResponse(u'Here is the ticketing center')

def download_list(request):
    qs = Rates.objects.all()
    return render_to_csv_response(qs,filename=u'Rates.csv')
    # qs = Tariffs.objects.get()
    # return render_to_csv_response(qs,filename=u'tariffs.csv')

def bills(request):
    if not request.user.is_authenticated:
        return redirect('/users/home')
    print('printing the url')
    print(request.get_full_path)
     
    username= request.user.username
    # testobject=Tariffs.objects.all()
    # testobject2=Tariffs.objects.filter(user_name=username)

    # for i in testobject:
    #     print("Printing testobjects :")
    #     print(i)
    # for c in testobject2:
    #     print("Printing testobject2 :")
    #     print(c)
    # print(username)
    query=Tariffs.objects.get(user_name=username)
    #    query=Tariffs.objects.all(user_name=username)
    # print(query.site_address)
    # print(query.user_name)
    # print('print start time')
    print(query.start_time)

    # print(datetime.now())
    userinfoobject= UserInfo.objects.get( user_name = username)
    if not userinfoobject.admin_bit:
      query.end_time= datetime.now()
    
    print(query.end_time)

    print(query.start_time.hour)
    print(query.end_time.hour)
    # print("Try to print seconds")
    # print(query.start_time.second)

    st_sec = query.start_time.second + query.start_time.minute*60 + query.start_time.hour*24*60

    et_sec = query.end_time.second+ query.end_time.minute*60 + query.end_time.hour*24*60
    # print("No of minutes is:")
    # print((et_sec-st_sec)//60)
    hoursspent = (et_sec-st_sec)//3600
    # print(query.start_time.minute)
    # print(query.end_time.second)
    # print(query.end_time.minute)
    #                                         print(hoursspent)
    # delta = datetime.combine(date.today(), query.endtime) - datetime.combine(date.today(), query.start_time)
    # delta_hours = delta.days * 24 + delta.seconds / 3600.0
    if(hoursspent>1):
        query.parking_money=hoursspent*query.per_hour_money
    else:
        query.parking_money=query.per_hour_money
    
    query.parking_time = hoursspent
    query.save()

    #                                            print(hoursspent)


    # print(query.parking_money)
    # print(query.start_time)
    # print("Rendering context ")

    context={
        'query':query
        
    }
    return render(request,'bills.html',context)

def download_csv(request):
    qs = Tariffs.objects.all()
    return render_to_csv_response(qs,filename=u'tariffs.csv')



        # Create the HttpResponse object with the appropriate CSV header.
    # response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="tariff.csv"'

    # writer = csv.writer(response)
    # writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    # writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    # qs = Tariffs.objects.values('user_name','car_number')