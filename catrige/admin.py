from django.contrib import admin
from catrige.models import *



@admin.register(Color)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Catriege)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ['category','serialNumber','modelProduct','date']

@admin.register(CatrigeModel)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ['model', 'color','firm']
