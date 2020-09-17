from django.urls import path
from catrige.views import *

urlpatterns = [
    path('',  catrigeInfo, name='catrige'),
    path('',  printSection, name='list'),
    path('section/',  catrigeSection, name='ctSection'),
]