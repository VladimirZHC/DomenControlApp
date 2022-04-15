# Generated by Django 3.2 on 2022-04-15 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Групповая политика')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Содержимое политики')),
            ],
            options={
                'verbose_name': 'Групповую политиику',
                'verbose_name_plural': 'Групповые политики',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ParamsSchema',
            fields=[
                ('type', models.SlugField(allow_unicode=True, choices=[('HOST', 'host'), ('USER', 'user')], default='HOST', max_length=10, primary_key=True, serialize=False, verbose_name='Типы')),
                ('body', models.TextField(blank=True, default='{}', null=True, verbose_name='Содержимое схемы')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.CreateModel(
            name='OrgUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Подразделение')),
                ('group_policies', models.ManyToManyField(blank=True, related_name='orgunits', to='control.GroupPolicy', verbose_name='групповые политики')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='control.orgunit', verbose_name='Подразделение')),
            ],
            options={
                'verbose_name': 'Подразделение',
                'verbose_name_plural': 'Подразделения',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Компьютеры')),
                ('orgunit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to='control.orgunit', verbose_name='Подразделение')),
            ],
            options={
                'verbose_name': 'Компьютер',
                'verbose_name_plural': 'Компьютеры',
            },
        ),
        migrations.CreateModel(
            name='HistoryParamsSchema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, default='{}', null=True, verbose_name='Содержимое схемы')),
                ('updated', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата изменения транзакции')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='control.paramsschema')),
            ],
            options={
                'verbose_name': 'Историю схемы параметров',
                'verbose_name_plural': 'Истории схемы параметров',
            },
        ),
        migrations.CreateModel(
            name='HistoryGroupPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Наименование политики')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Содержимое политики')),
                ('updated', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата изменения транзакции')),
                ('history_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='control.grouppolicy')),
            ],
            options={
                'verbose_name': 'Историю групповой политики',
                'verbose_name_plural': 'Истории групповой политики',
            },
        ),
        migrations.CreateModel(
            name='DomainUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя пользователя')),
                ('login', models.CharField(default='user1', max_length=20, unique=True, verbose_name='Логин пользователя')),
                ('orgunit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='control.orgunit', verbose_name='Подразделение')),
            ],
            options={
                'verbose_name': 'Пользователя',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
