from django.contrib import admin
from localization.models import *


@admin.register(Titul)
class Titul(admin.ModelAdmin):
    list_display = ['titulName']

@admin.register(Room)
class Room(admin.ModelAdmin):
    list_display = ('numberTitul','titul', 'numberRoom','flor')