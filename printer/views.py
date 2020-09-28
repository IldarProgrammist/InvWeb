from django.shortcuts import render
from django.views.generic import ListView
from printer.models import *
from django.db.models import Q
from django.views.generic.detail import DetailView

class PrinterInfoView(ListView):
    model = PtinterCatrige
    queryset = PtinterCatrige.objects.all()
    context_object_name = 'prModel'
    template_name = 'printer/printer_info.html'





def printerListView(request):

    searchQwery = request.GET.get('search', '')
    if searchQwery:
        printer = Printer.objects.filter(Q(serialNumber__contains=searchQwery))
    else:
        printer = Printer.objects.all()

    return render(request,'printer/printerList.html', context={'printer_': printer})




class PrinterDetailView(DetailView):
    model = Printer
    template_name = 'printer/listDetail.html'
