from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import request
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from catrige.models import *
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, DetailView, ListView
from .forms import CatrigeForm, CatrigeUpdateStatusForm, CatrigeJurnalCreateForm


@login_required
def refuelingCatrigeListView(request):
    refueling = Catriege.objects.filter(status__name='На заправку')
    return render(request,'catrige/refuelingCatrigeList.html', {'refueling': refueling} )


class CatrigeInfo(TemplateView):
    template_name = 'catrige/catrige_info.html'


@login_required
def catrigeSearchView(request):
    searchQwery = request.GET.get('search', '')
    if searchQwery:
        catrige = Catriege.objects.filter(Q(serialNumber__contains=searchQwery))
    else:
        catrige = Catriege.objects.all()
    return render(request, 'catrige/catrigeList.html', context={'catrige': catrige})





class CatrigeListView(ListView):
    model = Catriege
    queryset = Catriege.objects.all()
    template_name = 'catrige/catrigeList.html'
    context_object_name = 'catrige'

class CatrigeSearch(ListView):
    model = Catriege
    template_name = 'catrige/catrigeList.html'

    def get_queryset(self):
        searchQwery = request.GET.get('search', '')
        return Catriege.objects.filter(Q(serialNumber__contains=searchQwery))


class CatrigeDetile(DetailView):
    model = Catriege
    queryset = Catriege.objects.all()
    template_name = 'catrige/listDetile.html'
    context_object_name = 'catrige'


class CreateCatrigeView(CreateView):
    model = Catriege
    form_class =  CatrigeForm
    template_name = 'catrige/CreateCatrige.html'



class UppdateCatrige(UpdateView):
    model = Catriege
    form_class = CatrigeForm
    template_name = 'catrige/UpdateCatrige.html'
    # fields = '__all__'



class EditStatusCatrige(UpdateView):
    model = Catriege
    form_class = CatrigeUpdateStatusForm
    template_name = 'catrige/UpdateCatrige.html'



class DeleteCatrige(DeleteView):
    model = Catriege
    template_name = 'catrige/DeleteCatrige.html'
    success_url =  reverse_lazy('catrigeList')



class JurnalCarigeListView(ListView):
    model = CatrigeJurnal
    template_name = 'catrige/JurnalCarigeList.html'
    context_object_name = 'jcl'


class JurnlalCatrigeCreate(CreateView):
    model = CatrigeJurnal
    form_class = CatrigeJurnalCreateForm
    template_name = 'catrige/JurnalCreateCatrige.html'
    context_object_name = 'jcc'
