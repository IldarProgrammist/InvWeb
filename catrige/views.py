from django.shortcuts import render
from django.views.generic import ListView
from .models import Catriege

class ListCatrigeView(ListView):
    model = Catriege
    queryset = Catriege.objects.all()
    context_object_name = 'catrige'
    template_name = 'catrige/catrigesList.html'


def catrigeInfo(request):
    return render(request,'catrige/catrige.html')
