from django.urls import path
from catrige.views import *

urlpatterns = [
    path('',  CatrigeInfoView.as_view(), name='catrige'),
    path('list/', catrigeListView, name='catrigeList'),
    path('list/<int:pk>/', catrigeDetile,  name = 'catrige_detail'),
    path('refueling/', RefuelingCatrigeListView.as_view(), name='refueling')
]
