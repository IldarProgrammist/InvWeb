from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def homeView(request):
   return render(request, 'main/index.html')


@login_required
def printerView(request):
   return render(request, 'main/print.html')

