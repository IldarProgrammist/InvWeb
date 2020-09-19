from django.contrib import admin
from printer.models import *
from django import forms

@admin.register(PrinterModel)
class FirmAdmin(admin.ModelAdmin):
    pass


class PrinterChoiceField(forms.ModelChoiceField):
    pass

@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ['serialNumber', 'category', 'status']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return PrinterChoiceField(Category.objects.filter(slug='printer'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)








@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']

