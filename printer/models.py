from django.urls import reverse

from catrige.models import CatrigeModel
from main.models import *
from localization.models import *




class PrinterModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название модели принтера', unique=True)
    photo = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'Модель принтера'
        verbose_name_plural = 'Модели принтеров'

    def __str__(self):
        return self.name



class Firm(models.Model):
    name = models.CharField(max_length=100, verbose_name='Фирма')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Фирма принтера'
        verbose_name_plural = 'Фирмы принтеров'

    def __str__(self):
        return self.name


class ModelFirm(models.Model):
    number = models.IntegerField(verbose_name='Номер', unique=True, auto_created=True)
    firm = models.ForeignKey(Firm, models.CASCADE, verbose_name='Фирма')
    model = models.ForeignKey(PrinterModel, models.CASCADE, verbose_name='Модель принтера')

    def __str__(self):
        return "{} {}".format(self.firm.name, self.model.name)



class PtinterCatrige(models.Model):
    number = models.IntegerField(verbose_name='Номер', unique=True)
    printerModel = models.ForeignKey(PrinterModel, models.CASCADE, verbose_name='Модель принтера')

    def __str__(self):
        return "{} {}".format(self.printerModel.name, self.catrigeModel.name)


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
    discription = models.TextField(verbose_name='Описание')
    date_now = models.DateTimeField(auto_now_add=True,  verbose_name='Дата')

    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'

    def __str__(self):
        return self.serialNumber

    def get_absolute_url(self):
        return reverse('printerList')

