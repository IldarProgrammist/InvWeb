from django.urls import path
from printers.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', login_required(PrinterInfoView.as_view()), name='printer'),
    # path('list/', printerListView, name='printerList'),
    path('list/',login_required(PrinterListView.as_view()), name='printerList'),
    path('detile/<int:pk>/', login_required(PrinterDetileView.as_view()), name='printer_detail'),
    path('compatibility/', login_required(PrinterCatrigeView.as_view()),name = 'compatibility'),
    path('compatibility/<int:pk>/', login_required(PrinterCatrigeDetileView.as_view()), name='compatibility_detile'),
    path('printerinfo/<int:pk>/', login_required(PrintInfo.as_view()), name='printInfo'),
    path('jurnal/<int:pk>/', login_required(JurnalPrinterDetileView.as_view()), name = 'jurnal_printer_detile'),
    path('jurnal/create/', login_required(JurnalPrinterCreate.as_view()), name='create_jurnal_printer'),
    path('jurnal/', jurnalPrinterListView, name='jurnal_printer'),






    # path('jurnal/<int:pk>/', login_required(JurnalPrinterUpdateView.as_view()), name='update_jurnal_printer'),
    # path('update_printer_status/<int:pk>', login_required(EditStatusPrinter.as_view()), name='update_printer_status'),
    # path('list/<int:pk>/', printerDetile,  name = 'printer_detail'),

]