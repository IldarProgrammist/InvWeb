from django.contrib import admin
from printer.models import *
from django import forms

@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
    list = ['name']

@admin.register(PrinterModel)
class FirmAdmin(admin.ModelAdmin):
    list = ['name']

@admin.register(ModelFirm)
class ModelFirmAdmin(admin.ModelAdmin):
    list_display = ['firm','model']



class PrinterChoiceField(forms.ModelChoiceField):
    pass

@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ['serialNumber', 'category', 'status', 'date_now']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return PrinterChoiceField(Category.objects.filter(slug='printer'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']

