from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from printer.models import *


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

    return render(request, 'printer/printerList.html', context={'printer_': printer})


class PrinterDetailView(DetailView):
    template_name = 'printer/listDetail.html'


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Printer, id=id_)
