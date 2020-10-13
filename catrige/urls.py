from django.urls import path
from catrige.views import *

urlpatterns = [
    path('', catrigeInfoView,name='catrige'),
    path('list/', catrigeListView, name='catrigeList'),
    path('list/<int:pk>/', catrigeDetile,  name = 'catrige_detail'),
    path('refueling/', refuelingCatrigeListView, name='refueling')


]
