from django.urls import path
from . import views

urlpatterns = [
    path('accounts_index',views.accounts_index,name='accounts_index'),
]