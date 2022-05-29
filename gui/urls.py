from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name='home'),
    path('result/', result, name='result'),
    path('predict',predict,name='predict'),
    path('dv',dv,name='dv'),
    path('sales',sales,name='sales'),
]
