
from django.views.generic import ListView
from .models import Catriege

class ListCatrigeView(ListView):
    model = Catriege
    queryset = Catriege.objects.all()
    context_object_name = 'catrige'
    template_name = 'catrige/catriges.html'

