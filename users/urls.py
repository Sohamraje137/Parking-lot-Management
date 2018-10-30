from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('user_detail',views.user_detail,name='user_detail'),
]