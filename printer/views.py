from django.shortcuts import render
from django.views.generic import ListView
from printer.models import *
from django.db.models import Q

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

def printerListView(request):

    searchQwery = request.GET.get('search', '')
    if searchQwery:
        printer = Printer.objects.filter(Q(serialNumber__contains=searchQwery))
    else:
        printer = Printer.objects.all()

    return render(request,'printer/printerLocation.html', context={'printer_': printer})




# class SearchPrinter(ListView):
#     model = Printer
#     template_name = 'printer/search_results.html'
#     context_object_name = 'printers'
