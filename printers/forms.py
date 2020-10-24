from django import forms
from printers.models import JurnalPrinter, Printer



class PrinterJurnalForm(forms.ModelForm):

    class Meta:
        model = JurnalPrinter
        fields =('status','date','discription')

        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'date':   forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'discription':forms.TextInput(attrs={'class':'form-control'})
        }



class PrinterJurnalCreateForm(forms.ModelForm):
    class Meta:
        model = JurnalPrinter
        fields ='__all__'

        widgets = {
            'appeal': forms.TextInput(attrs={'class': 'form-control'}),
            'serialNumber': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'discription': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.SelectDateWidget(attrs={'class': 'form-control'}),

        }

class PrinterJurnalStatusForm(forms.ModelForm):
    class Meta:
        model = JurnalPrinter
        fields = '__all__'

        widgets = {
            'status': forms.Select(attrs={'class':'form-control'})
        }