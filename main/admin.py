from django.contrib import admin
from main.models import *

@admin.register(Firms)
class FirmAdmin(admin.ModelAdmin):
    list_display = ['name']
