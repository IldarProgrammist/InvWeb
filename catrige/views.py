from django.shortcuts import render
from django.views.generic import *
from catrige.models import *


def catrigeInfo(request):
    return render(request,'catrige/catrige.html')

def printSection(request):
    return render(request,'catrige/carigeSpace.html')


class CatrigeSectionView(ListView):
    model = CatrigeModel
    context_object_name = 'ctSection'
    template_name = 'catrige/carigeSpace.html'



class CarigeModelView(ListView):
    model = CatrigeModel
    context_object_name = 'ctModel'
    template_name = 'catrige/catreigModels.html'


