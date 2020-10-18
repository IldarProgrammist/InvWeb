from django.urls import path
from printers.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', login_required(PrinterInfoView.as_view()), name='printer'),
    path('list/', printerListView, name='printerList'),
    path('detile/<int:pk>/', login_required(PrinterDetileView.as_view()), name='printer_detail'),
    path('create/', login_required(CreatePrinterView.as_view()), name='create_printer'),
    path('update_printer_status/<int:pk>', login_required(EditStatusPrinter.as_view()), name='update_printer_status'),
    path('compatibility/', login_required(PrinterCatrigeView.as_view()),name = 'compatibility'),
    path('compatibility/<int:pk>/', login_required(PrinterCatrigeDetileView.as_view()), name='compatibility_detile')





    # path('list/<int:pk>/', printerDetile,  name = 'printer_detail'),

]