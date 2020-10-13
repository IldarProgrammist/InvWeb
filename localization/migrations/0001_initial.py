# Generated by Django 3.1.1 on 2020-10-12 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Titul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulName', models.CharField(max_length=100, unique=True, verbose_name='Название титула')),
            ],
            options={
                'verbose_name': 'Титул',
                'verbose_name_plural': 'Титулы',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberTitul', models.CharField(max_length=20, verbose_name='Номер титула')),
                ('numberRoom', models.CharField(max_length=10, unique=True, verbose_name='Номер кабинета')),
                ('flor', models.IntegerField(verbose_name='Этаж')),
                ('discription', models.TextField(blank=True, verbose_name='Премечание')),
                ('titul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localization.titul', verbose_name='Нахвание титула')),
            ],
            options={
                'verbose_name': 'Кабинет',
                'verbose_name_plural': 'Кабинеты',
            },
        ),
    ]