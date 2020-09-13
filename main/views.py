from django.views.generic import *

from main.models import Category


class HomeView(ListView):
   template_name = 'main/index.html'
   queryset = Category

