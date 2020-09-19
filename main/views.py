from django.shortcuts import render
from django.views.generic import *

from main.models import Category


class HomeView(ListView):
   template_name = 'main/index.html'
   queryset = Category


def pintView(request):
   return render(request, 'main/print.html')
