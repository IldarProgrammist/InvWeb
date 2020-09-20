from django.views.generic import ListView
from printer.models import *


class PrinterInfoView(ListView):
    model = PtinterCatrige
    queryset = PtinterCatrige.objects.all()
    context_object_name = 'prModel'
    template_name = 'printer/printer_info.html'




class PrinterList(ListView):
    model = Printer
    queryset = Printer.objects.all()
    context_object_name = 'PrinterList'
    template_name = 'printer/PrinterList.html'

class PrinterLocation(ListView):
    model = Printer
    queryset = Printer.objects.all()
    context_object_name = 'PrinterList'
    template_name = 'printer/printerLocation.html'
