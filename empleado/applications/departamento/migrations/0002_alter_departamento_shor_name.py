# Generated by Django 4.0.4 on 2022-05-29 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='shor_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nombre Corto'),
        ),
    ]