# Generated by Django 3.2.8 on 2024-07-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_auto_20240701_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='dinner_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Обед'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='dinner_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Обед'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='dinner_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Обед'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='monday_friday_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Понедельник - пятницы'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='monday_friday_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Понедельник - пятницы'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='monday_friday_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Понедельник - пятницы'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='saturday_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Суббота'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='saturday_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Суббота'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='saturday_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Суббота'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='schedule_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='График работы'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='schedule_title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='График работы'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='schedule_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='График работы'),
        ),
    ]
