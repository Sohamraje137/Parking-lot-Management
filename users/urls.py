from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('Checkoutuser',views.Checkoutuser,name='Checkoutuser'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout, name= 'logout'),
    path('emptyslot/<slug:username>',views.emptyslot,name='emptyslot'),
    path('user_detail',views.user_detail,name='user_detail'),
]