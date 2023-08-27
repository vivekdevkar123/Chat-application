from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('<str:group_name>/',index,name='index'),
    path('result/output/', Output, name='output'),
]