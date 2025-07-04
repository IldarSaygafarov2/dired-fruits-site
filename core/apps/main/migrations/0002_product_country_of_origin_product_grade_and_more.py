# Generated by Django 5.2 on 2025-06-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country_of_origin',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Страна происхождения'),
        ),
        migrations.AddField(
            model_name='product',
            name='grade',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='production_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата производства'),
        ),
    ]
