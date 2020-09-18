from django.contrib import admin
from catrige.models import *
from django import  forms


@admin.register(Color)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','word']




class CatrigeChoiceField(forms.ModelChoiceField):
    pass



@admin.register(Catriege)
class CatrigeAdmin(admin.ModelAdmin):
    list_display = ['serialNumber','modelProduct','status','date']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return CatrigeChoiceField(Category.objects.filter(slug = 'catrige'))
        return  super().formfield_for_foreignkey(db_field, request, **kwargs)



@admin.register(CatrigeModel)
class CatrigeModelAdmin(admin.ModelAdmin):
    list_display = ['model', 'color','firm']

@admin.register(PrinterCatrigeCompatibility)
class CatrigeCatrigeCompatibilityAdmin(admin.ModelAdmin):
    list_display = ['number', 'printer','model']

@admin.register(Status)
class CatrigeStatusAdmin(admin.ModelAdmin):
    list_display = ['name']
