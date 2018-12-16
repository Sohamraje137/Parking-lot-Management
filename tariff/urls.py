from django.urls import path
from . import views
from .models import Tariffs
urlpatterns = [
    path('index/<int:site_num>',views.index,name='index'),
    path('download_csv',views.download_csv,name='download_csv'),
    path('rates',views.download_list,name='download_list'),
    path('bills',views.bills,name='personal bills'),
]