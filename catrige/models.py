from main.models import *


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


class Catriege(Products):
    pass

    class Meta:
        verbose_name = 'Картридж'
        verbose_name_plural = 'Картриджи'

    def __str__(self):
        return self.serialNumber







