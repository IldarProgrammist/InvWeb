from django.urls import path
from printer.views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [

    path('', login_required(PrinterInfoView.as_view()), name='printer'),
    path('list/', printerListView, name='printerList'),
    path('detile/<int:pk>/', login_required(PrinterDetileView.as_view()),  name = 'printer_detail'),
    path('create/', login_required(CreatePrinterView.as_view()), name='create_printer' ),
    path('update_printer_status/<int:pk>', login_required(EditStatusPrinter.as_view()), name = 'update_printer_status'),
    # path('list/<int:pk>/', printerDetile,  name = 'printer_detail'),

]

