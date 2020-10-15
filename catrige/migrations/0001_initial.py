# Generated by Django 3.1.1 on 2020-10-12 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Цвет')),
                ('word', models.CharField(max_length=1, unique=True, verbose_name='Обозначение')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус картриджа',
                'verbose_name_plural': 'Статусы картриджей',
            },
        ),
        migrations.CreateModel(
            name='CatrigeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название модели картриджа')),
                ('fhoto', models.ImageField(blank=True, upload_to='', verbose_name='Фото')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catrige.color', verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Модель картриджа',
                'verbose_name_plural': 'Модели картриджей',
            },
        ),
        migrations.CreateModel(
            name='Catriege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialNumber', models.CharField(max_length=40, unique=True, verbose_name='Серийный номер')),
                ('date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория оборудования')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catrige.catrigemodel', verbose_name='Модель картриджа')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catrige.status', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Картридж',
                'verbose_name_plural': 'Картриджи',
            },
        ),
    ]