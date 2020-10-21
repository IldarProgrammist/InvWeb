from django.db import models
from catrige.models import *
from localization.models import Room


class Firm(models.Model):
    name = models.CharField(max_length=100, verbose_name='Фирма')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Фирма принтера'
        verbose_name_plural = 'Фирмы принтеров'

    def __str__(self):
        return self.name

class PrinterModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название модели принтера', unique=True)
    photo = models.ImageField(blank=True)
    firm = models.ForeignKey(Firm, models.CASCADE, verbose_name='Фирма принтера')
    catrige = models.ManyToManyField(CatrigeModel, verbose_name='Катридж', blank=True, related_name='CatrigeModel')

    class Meta:
        verbose_name = 'Модель принтера'
        verbose_name_plural = 'Модели принтеров'

    def __str__(self):
        return self.name



class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус')

    class Meta:
        verbose_name = 'Статус принтера'
        verbose_name_plural = 'Статусы принтеров'

    def __str__(self):
        return self.name



class Printer(Products):
    printerModel = models.ForeignKey(PrinterModel, on_delete=models.CASCADE, verbose_name='Модель принтера')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Локация')
    ip = models.CharField(max_length=30, verbose_name='IP-адрес', blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус принтера')
    discription = models.TextField(verbose_name='Описание',blank=True)
    date_now = models.DateTimeField(verbose_name='Дата')

    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'

    def __str__(self):
        return self.serialNumber

    def get_absolute_url(self):
        return reverse('printerList')