# Generated by Django 3.2.8 on 2024-07-01 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_auto_20240701_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialnetwork',
            name='page_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='socialnetwork',
            name='page_title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='socialnetwork',
            name='page_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
    ]
