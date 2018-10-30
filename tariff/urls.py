from django.urls import path
from . import views
urlpatterns = [
    path('index/<int:site_num>',views.index,name='index'),
    path('download_csv',views.download_csv,name='download_csv')
]