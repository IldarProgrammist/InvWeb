from django.urls import path
from catrige.views import *

urlpatterns = [
    path('', catrigeInfoView,name='catrige'),
    path('list/', catrigeListView, name='catrigeList'),
    path('list/<int:pk>/', catrigeDetile,  name = 'catrige_detail'),
    path('refueling/', refuelingCatrigeListView, name='refueling'),
    path('add_catrige/', AddCatrigeView.as_view(), name='add_catrege'),
    path('update_catrige/<int:pk>/', UppdateCatrige.as_view(),name = 'update_catrige'),
    path('update_catrige_status/<int:pk>', EditStatusCatrige.as_view(), name = 'update_catrige_status')

]
