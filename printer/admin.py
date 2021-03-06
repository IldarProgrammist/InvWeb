from django.contrib import admin
from printer.models import *


@admin.register(PrinterModel)
class FirmAdmin(admin.ModelAdmin):
    list_display = ['model', 'firm']


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ['category', 'serialNumber','modelProduct','status']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']

