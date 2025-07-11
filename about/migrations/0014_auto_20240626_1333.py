# Generated by Django 3.2.8 on 2024-06-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0013_auto_20240626_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='vision',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='vision',
            name='text_ky',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='vision',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='vision',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='vision',
            name='title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='vision',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
    ]
