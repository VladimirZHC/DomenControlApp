# Generated by Django 3.2 on 2022-03-18 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='division',
            name='types',
            field=models.ManyToManyField(blank=True, related_name='types', to='control.SchemaParams', verbose_name='Тип'),
        ),
    ]
