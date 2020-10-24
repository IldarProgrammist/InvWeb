from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import request
from django.shortcuts import render, get_object_or_404
from django.views.generic import *
from printers.forms import PrinterJurnalCreateForm, PrinterJurnalStatusForm
from printers.models import PrinterModel, JurnalPrinter, Printer


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


@login_required
def jurnalPrinterListView(request):

    searchQwery = request.GET.get('search', '')
    if searchQwery:
        jurnalPrinter = JurnalPrinter.objects.filter(Q(status__name =searchQwery) | Q(serialNumber__serialNumber__icontains =searchQwery) )
    else:
        jurnalPrinter = JurnalPrinter.objects.all()
    return render(request, 'printer/JurnalListPrinter.html', context={'jpl': jurnalPrinter})




class JurnalPrinterDetileView(DetailView):
    model = JurnalPrinter
    template_name = 'printer/JurnalDetile.html'
    context_object_name = 'jpd'


class JurnalPrinterCreate(CreateView):
    model = JurnalPrinter
    form_class =  PrinterJurnalCreateForm
    template_name = 'printer/JurnalPrinterCreate.html'
    context_object_name = 'jplc'














# class JurnalPrinterUpdateView(UpdateView):
#     model = JurnalPrinter
#     form_class = PrinterJurnalForm
#     template_name = 'printer/JurnalUpdate.html'
#     context_object_name = 'jplu'




