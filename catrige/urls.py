from django.urls import path
from catrige.views import *

urlpatterns = [
    path('',  printSection, name='list'),
    path('section/',  CatrigeSectionView.as_view(), name='ctSection'),

]
