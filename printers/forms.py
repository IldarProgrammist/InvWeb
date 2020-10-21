from django import forms
from .models import Printer

class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = ('category','printerModel', 'serialNumber','ip', 'room', 'status')

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'printerModel': forms.Select(attrs={'class': 'form-control'}),
            'serialNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'ip': forms.TextInput(attrs={'class': 'form-control'}),
            'room': forms.Select(attrs={'class': 'form-control'}),
            'status':forms.Select(attrs={'class': 'form-control'}),
        }



class PrinterUpdateStatusForm(forms.ModelForm):
        class Meta:
            model = Printer
            fields = ('serialNumber', 'status','discription','date_now')

            widgets = {
                    'serialNumber': forms.TextInput(attrs={'class': 'form-control'}),
                    'status': forms.Select(attrs={'class': 'form-control'}),
                    'discription': forms.TextInput(attrs={'class': 'form-control'}),
                    'date_now':forms.SelectDateWidget(attrs={'class': 'form-control'})
                }