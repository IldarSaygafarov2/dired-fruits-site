# Generated by Django 5.2 on 2025-06-21 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название категории')),
                ('description', models.TextField(blank=True, verbose_name='Описание категории')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='categories/icons/', verbose_name='Иконка категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=200, verbose_name='Название товара')),
                ('description', models.TextField(blank=True, verbose_name='Описание товара')),
                ('price', models.FloatField(default=0.0, verbose_name='Цена товара')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/images/', verbose_name='Изображение товара')),
                ('manufacturer', models.CharField(blank=True, max_length=200, null=True, verbose_name='Производитель')),
                ('importer', models.CharField(blank=True, max_length=200, null=True, verbose_name='Импортер')),
                ('net_weight', models.IntegerField(blank=True, null=True, verbose_name='Нетто вес')),
                ('gross_weight', models.IntegerField(blank=True, null=True, verbose_name='Брутто вес')),
                ('batch_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер партии')),
                ('storage_conditions', models.TextField(blank=True, null=True, verbose_name='Условия хранения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'abstract': False,
            },
        ),
    ]
