from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')

    class Meta:
        verbose_name ='Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Firms(models.Model):
    name = models.CharField(max_length=50, verbose_name='Фирма', unique= True)

    class Meta:
        verbose_name ='Фирма'
        verbose_name_plural = 'Фирмы'

    def __str__(self):
        return self.name

class Models(models.Model):
    model = models.CharField(max_length=50, verbose_name='Модель', unique=True)
    firm = models.ForeignKey(Firms, models.CASCADE, verbose_name='Фирма')
    fhoto = models.ImageField(verbose_name='Фото', blank=True)

    def __str__(self):
        return self.model



class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория оборудования')
    serialNumber = models.CharField(max_length=40, verbose_name='Серийный номер', unique=True)
    modelProduct = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель')

    date = models.DateField()
    class Meta:
        abstract = True
