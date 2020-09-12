from django.db import models

from django.db import models


class Titul(models.Model):
    titulName = models.CharField(max_length=100, verbose_name='Название титула', unique=True)

    def __str__(self):
        return self.titulName

    class Meta:
        verbose_name  = 'Титул'
        verbose_name_plural = 'Титулы'

class Room(models.Model):
    numberTitul = models.CharField(max_length=20, verbose_name='Номер титула')
    titul = models.ForeignKey(Titul, on_delete=models.CASCADE, verbose_name='Нахвание титула')
    numberRoom = models.CharField(max_length=10, verbose_name='Номер кабинета', unique=True)
    flor = models.IntegerField(verbose_name='Этаж')
    discription = models.TextField(verbose_name='Премечание',blank=True)

    def __str__(self):
        return self.numberRoom

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural  = 'Кабинеты'
