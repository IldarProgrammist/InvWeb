from django.urls import path
from catrige.views import *

urlpatterns = [
    path('',  CatrigeInfoView.as_view(), name='catrige'),
]
