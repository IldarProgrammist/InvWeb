from django.urls import path
from catrige.views import *

urlpatterns = [
    path('',  catrigeInfo, name='catrige'),
    path('List/', ListCatrigeView.as_view(), name='catrigeList'),
]