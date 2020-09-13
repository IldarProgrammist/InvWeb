from main.models import *
from printer.models import *


class Color(models.Model):
    name = models.CharField(max_length=30, verbose_name='Цвет', unique=True)
    word = models.CharField(max_length=1, verbose_name='Обозначение', unique=True)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


    def __str__(self):
        return self.name

class CatrigeModel(Models):
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Цвет')

    class Meta:
        verbose_name = 'Модель картриджа'
        verbose_name_plural = 'Модели картриджей'

    def __str__(self):
        return self.model


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус')


    class Meta:
        verbose_name = 'Статус картриджа'
        verbose_name_plural = 'Статусы картриджей'

    def __str__(self):
        return self.name



class Catriege(Products):

    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    date = models.DateField()

    class Meta:
        verbose_name = 'Картридж'
        verbose_name_plural = 'Картриджи'

    def __str__(self):
        return self.serialNumber


"""Совместимость принтера и картриджа"""

class PrinterCatrigeCompatibility(models.Model):
    number = models.CharField(max_length=50, verbose_name="Номер", unique=True)
    printer = models.ForeignKey(PrinterModel, on_delete=models.CASCADE, verbose_name='Модель принтера')
    model = models.ForeignKey(CatrigeModel, on_delete=models.CASCADE, verbose_name='Модель картриджа')

    class Meta:
        verbose_name = 'Совместимость картриджа'
        verbose_name_plural = 'Совместимость картриджей'

    def __str__(self):
        return self.number



