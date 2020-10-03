from django.urls import path
from printer.views import *

urlpatterns = [
    path('',  PrinterInfoView.as_view(), name='printer'),
    path('list/', printerListView, name='printerList'),
    # path('list/detile/<int:pk>', name = 'detile'),
    path('list/<int:pk>/', printerDetile,  name = 'printer_detail'),

    # path('detile/<int:pk>/', PrinterDetailView.as_view(), name='printer-detile')
]

