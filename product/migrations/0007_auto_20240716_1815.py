# Generated by Django 3.2.8 on 2024-07-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20240716_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='category_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Наименование категории'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category_title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Наименование категории'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Наименование категории'),
        ),
    ]
