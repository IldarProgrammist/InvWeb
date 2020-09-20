from django.urls import path
from printer.views import *

urlpatterns = [
    path('',  PrinterInfoView.as_view(), name='printer'),
    path('list/', PrinterList.as_view(), name='printerList'),
    path('location/', PrinterLocation.as_view(), name='printerLocation')

]

