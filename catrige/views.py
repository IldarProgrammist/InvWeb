from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from catrige.models import *
from django.views.generic import  CreateView
@login_required
def refuelingCatrigeListView(request):
    refueling = Catriege.objects.filter(status__name='На заправку')
    return render(request,'catrige/refuelingCatrigeList.html', {'refueling': refueling} )


@login_required
def catrigeInfoView(request):
    return render(request, 'catrige/catrige_info.html')


@login_required
def catrigeListView(request):
    searchQwery = request.GET.get('search', '')
    if searchQwery:
        catrige = Catriege.objects.filter(Q(serialNumber__contains=searchQwery))
    else:
        catrige = Catriege.objects.all()
    return render(request, 'catrige/catrigeList.html', context={'catrige': catrige})


@login_required
def catrigeDetile(request, pk):
    catrige = get_object_or_404(Catriege, pk=pk)
    return render(request, 'catrige/listDetile.html', {'catrige': catrige})



class AddCatrigeView(CreateView):
    model = Catriege
    template_name = 'catrige/CreateCatrige.html'
    fields = '__all__'




