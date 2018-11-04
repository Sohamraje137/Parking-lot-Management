
import csv
from djqscsv import render_to_csv_response
from django.shortcuts import render
from django.http import HttpResponse
from tariff.models import Tariffs,Rates
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return HttpResponse(u'Here is the ticketing center')

def download_list(request):
    qs = Rates.objects.all()
    return render_to_csv_response(qs,filename=u'Rates.csv')
    # qs = Tariffs.objects.get()
    # return render_to_csv_response(qs,filename=u'tariffs.csv')

def download_personal_csv(request,username):
    if not request.user.is_authenticated:
        return redirect('/users/home')
 
    query=Tariffs.objects.filter(user_name=username)
    print(query)
    # print(query.car_number)
    # print(query.start_time)
    return render_to_csv_response(query,filename=u'Bill.csv')

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