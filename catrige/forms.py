from django import forms
from .models import Catriege

class CatrigeForm(forms.ModelForm):
    class Meta:
        model = Catriege
        fields = ('__all__')

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'serialNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.Select(attrs={'class': 'form-control'}),
            'status':forms.Select(attrs={'class': 'form-control'}),
        }

class CatrigeUpdateStatusForm(forms.ModelForm):
    class Meta:
        model = Catriege
        fields = ('serialNumber', 'status')

        widgets = {
            'serialNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
