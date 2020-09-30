from django.urls import path
from printer.views import *

urlpatterns = [
    path('',  PrinterInfoView.as_view(), name='printer'),
    path('list/', printerListView, name='printerList'),
    path('detile/<int:id>/', PrinterDetailView.as_view(), name = 'printer-detile')
]

