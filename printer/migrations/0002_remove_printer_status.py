# Generated by Django 3.0.8 on 2020-09-12 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('printer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='printer',
            name='status',
        ),
    ]
