from django import forms
from .models import Catriege, CatrigeJurnal


class CatrigeForm(forms.ModelForm):
    class Meta:
        model = Catriege
        fields = ('__all__')

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'serialNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.Select(attrs={'class': 'form-control'}),
        }





class CatrigeJurnalCreateForm(forms.ModelForm):
    class Meta:
        model = CatrigeJurnal
        fields ='__all__'

        widgets = {
            'appeal': forms.TextInput(attrs={'class': 'form-control'}),
            'serialNumber': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'discription': forms.TextInput(attrs={'class': 'form-control'}),


        }
