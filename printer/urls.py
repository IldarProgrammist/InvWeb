from django.urls import path
from printer.views import *

urlpatterns = [
    path('printers/',  PrinterInfoView.as_view(), name='printer'),

]

