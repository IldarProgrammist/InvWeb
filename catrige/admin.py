from django.contrib import admin
from catrige.models import *



@admin.register(Color)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','word']


@admin.register(Catriege)
class CatrigeAdmin(admin.ModelAdmin):
    list_display = ['serialNumber','modelProduct','status','date']

@admin.register(CatrigeModel)
class CatrigeModelAdmin(admin.ModelAdmin):
    list_display = ['model', 'color','firm']

@admin.register(PrinterCatrigeCompatibility)
class CatrigeCatrigeCompatibilityAdmin(admin.ModelAdmin):
    list_display = ['number', 'printer','model']

@admin.register(Status)
class CatrigeStatusAdmin(admin.ModelAdmin):
    list_display = ['name']
