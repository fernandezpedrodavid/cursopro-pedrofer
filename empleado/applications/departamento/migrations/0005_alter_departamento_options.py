# Generated by Django 4.0.4 on 2022-06-03 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0004_alter_departamento_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['-name'], 'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamento'},
        ),
    ]
