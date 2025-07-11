# Generated by Django 3.2.8 on 2024-07-17 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20240716_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='compound_en',
            field=models.TextField(blank=True, null=True, verbose_name='Состав'),
        ),
        migrations.AddField(
            model_name='products',
            name='compound_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Состав'),
        ),
        migrations.AddField(
            model_name='products',
            name='compound_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Состав'),
        ),
        migrations.AddField(
            model_name='products',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='products',
            name='description_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='products',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='products',
            name='fact_en',
            field=models.TextField(blank=True, null=True, verbose_name='Факт'),
        ),
        migrations.AddField(
            model_name='products',
            name='fact_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Факт'),
        ),
        migrations.AddField(
            model_name='products',
            name='fact_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Факт'),
        ),
    ]
