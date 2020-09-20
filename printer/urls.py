from django.urls import path
from printer.views import *

urlpatterns = [
    path('',  PrinterInfoView.as_view(), name='printer'),

]

