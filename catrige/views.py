from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from catrige.models import *


class CatrigeInfoView(ListView):
    model = CatrigeModel
    queryset = CatrigeModel.objects.all()
    context_object_name = 'catrige'
    template_name = 'catrige/catrige_info.html'



def catrigeListView(request):
    searchQwery = request.GET.get('search', '')
    if searchQwery:
        catrige = Catriege.objects.filter(Q(serialNumber__contains=searchQwery))
    else:
        catrige = Catriege.objects.all()
    return render(request, 'catrige/catrigeList.html', context={'catrige': catrige})


def catrigeDetile(request, pk):
    catrige = get_object_or_404(Catriege, pk=pk)
    return render(request, 'catrige/listDetile.html', {'catrige': catrige})


class RefuelingCatrigeListView(ListView):
    model = Catriege
    queryset =Catriege.objects.filter(status__name='На заправку')
    template_name = 'catrige/refuelingCatrigeList.html'
    context_object_name = 'refueling'



