from django.urls import path
from printer.views import *

urlpatterns = [
    # path('',  PrinterInfoView.as_view(), name='printer'),
    path('', printerInfoView, name='printer'),
    path('list/', printerListView, name='printerList'),
    path('list/<int:pk>/', printerDetile,  name = 'printer_detail'),
]

