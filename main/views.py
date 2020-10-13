from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView

#
# class HomeViews(TemplateView):
#    template_name = 'main/index.html'


@login_required
def homeView(request):
   return render(request, 'main/index.html')





# class MainView(TemplateView):
#    template_name = 'main/index.html'

class PrintView(TemplateView):
   template_name = 'main/print.html'

