from main.models import *
from localization.models import *

class PrinterModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название модели принтера')
    firm = models.ForeignKey(Firms, models.CASCADE, verbose_name='Фирма')
    photo = models.ImageField(blank=True)

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
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Локация')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус принтера')

    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'

    def __str__(self):
        return self.serialNumber