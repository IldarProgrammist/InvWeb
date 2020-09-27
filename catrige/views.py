from django.views.generic import ListView
from catrige.models import CatrigeModel


class CatrigeInfoView(ListView):
    model = CatrigeModel
    queryset = CatrigeModel.objects.all()
    context_object_name = 'catrige'
    template_name = 'catrige/catrige_info.html'





