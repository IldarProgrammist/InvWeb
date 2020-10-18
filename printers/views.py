from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import *

from printers.forms import PrinterForm, PrinterUpdateStatusForm
from printers.models import Printer, PrinterModel


class PrinterInfoView(TemplateView):
    template_name = 'printer/printer_info.html'


@login_required
def printerListView(request):
    searchQwery = request.GET.get('search', '')
    if searchQwery:
        printer = Printer.objects.filter(Q(serialNumber__contains=searchQwery))
    else:
        printer = Printer.objects.all()

    return render(request, 'printer/printerList.html', context={'printer_': printer})


class PrinterDetileView(DetailView):
    model = Printer
    queryset = Printer.objects.all()
    template_name = 'printer/listDetail.html'
    context_object_name = 'printer'


class PrinterCatrigeView(ListView):
    model = PrinterModel
    template_name = 'printer/compatibilityList.html'
    context_object_name = 'printerCatrige'


class PrinterCatrigeDetileView(DetailView):
    model = PrinterModel
    template_name = 'printer/compatibilityDetil.html'
    context_object_name = 'printerCatrige'




class PrintInfo(DetailView):
    model = PrinterModel
    template_name = 'printer/information.html'
    context_object_name = 'printerInformation'



class CreatePrinterView(CreateView):
    model = Printer
    form_class =  PrinterForm
    template_name = 'printer/CreatePrinter.html'


class EditStatusPrinter(UpdateView):
    model = Printer
    form_class = PrinterUpdateStatusForm
    template_name = 'catrige/UpdateCatrige.html'


@login_required
def printerDetile(request,pk ):
    prtinter = get_object_or_404(Printer, pk = pk)
    return render(request, 'printer/listDetail.html',{'printer':prtinter})



@login_required
def printerListView(request):
    searchQwery = request.GET.get('search', '')
    if searchQwery:
        printer = Printer.objects.filter(Q(serialNumber__contains=searchQwery))
    else:
        printer = Printer.objects.all()

    return render(request, 'printer/printerList.html', context={'printer_': printer})


