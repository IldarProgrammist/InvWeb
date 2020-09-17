from django.shortcuts import render


def catrigeInfo(request):
    return render(request,'catrige/catrige.html')

def printSection(request):
    return render(request,'catrige/carigeSpace.html')

def catrigeSection(request):
    return render(request,'catrige/carigeSpace.html')
