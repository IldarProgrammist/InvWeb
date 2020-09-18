from django.urls import path
from catrige.views import *

urlpatterns = [
    path('',  catrigeInfo, name='catrige'),
    path('',  printSection, name='list'),
    path('section/',  CatrigeSectionView.as_view(), name='ctSection'),
    path('model/',  CarigeModelView.as_view(), name='ctModel'),

]
