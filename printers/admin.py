from django.contrib import admin
from .models import *
from django import forms

@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
    list = ['name']

@admin.register(PrinterModel)
class PrinterModelAdmin(admin.ModelAdmin):
    list = ['name', 'firm']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list = ['name']


class PrinterChoiceField(forms.ModelChoiceField):
    pass

@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ['serialNumber', 'category']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return PrinterChoiceField(Category.objects.filter(slug='printer'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(JurnalPrinter)
class JurnalPrinterAdmin(admin.ModelAdmin):
    list_display = ['appeal', 'serialNumber', 'status', 'date']
