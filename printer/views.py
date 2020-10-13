from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from printer.models import *


@login_required
def printerInfoView(request):
    return render(request, 'printer/printer_info.html')


@login_required
def printerListView(request):
    searchQwery = request.GET.get('search', '')
    if searchQwery:
        printer = Printer.objects.filter(Q(serialNumber__contains=searchQwery))
    else:
        printer = Printer.objects.all()

    return render(request, 'printer/printerList.html', context={'printer_': printer})

@login_required
def printerDetile(request,pk ):
    prtinter = get_object_or_404(Printer, pk = pk)
    return render(request, 'printer/listDetail.html',{'printer':prtinter})


