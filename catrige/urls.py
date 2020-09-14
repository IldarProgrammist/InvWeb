from django.urls import path
from catrige.views import *

urlpatterns = [
    path('', ListCatrigeView.as_view(), name='catrige'),
]