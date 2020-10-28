from django.urls import path
from catrige.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(CatrigeInfo.as_view()), name='catrige' ),
    path('list/<int:pk>/',login_required(CatrigeDetile.as_view()),  name ='catrige_detail'),
    path('create/', login_required(CreateCatrigeView.as_view()) , name='add_catrege'),
    path('update/<int:pk>/', login_required(UppdateCatrige.as_view()) ,name = 'update_catrige'),
    path('delete/<int:pk>/', login_required(DeleteCatrige.as_view()), name = 'delete_catrige'),
    path('refueling/',refuelingCatrigeListView, name='refueling'),
    path('list/', catrigeSearchView, name='catrigeList'),
    path('list/', CatrigeListView.as_view(), name='catrigeList'),
    path('jurnal/', login_required(JurnalCarigeListView.as_view()), name='jurnal_catrige_list'),
    path('jurnal/create/', login_required(JurnlalCatrigeCreate.as_view()) , name = 'jurnal_catrige_create')

]
