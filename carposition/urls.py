from django.urls import path,include
from . import views

urlpatterns = [
    path('index/',views.car_site_index,name='car_site_index'),
    path('book/<int:site_no>',views.site_position_book, name='site_position_book'),

    path('order_position/<int:site_no>/<posi_num>',views.order_position,name='order_position'),
    path('download',views.download_positions,name='download'),
]