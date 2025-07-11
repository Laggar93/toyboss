# Generated by Django 3.2.8 on 2024-09-23 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0025_auto_20240704_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='email',
            field=models.CharField(default=1, max_length=255, verbose_name='Ваш email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactform',
            name='main_title',
            field=models.CharField(max_length=255, verbose_name='Остались вопросы'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='main_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Остались вопросы'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='main_title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Остались вопросы'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='main_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Остались вопросы'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='subtitle',
            field=models.TextField(verbose_name='Подзаголовок (Задайте интересующий вас вопрос...)'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='subtitle_en',
            field=models.TextField(null=True, verbose_name='Подзаголовок (Задайте интересующий вас вопрос...)'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='subtitle_ky',
            field=models.TextField(null=True, verbose_name='Подзаголовок (Задайте интересующий вас вопрос...)'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='subtitle_ru',
            field=models.TextField(null=True, verbose_name='Подзаголовок (Задайте интересующий вас вопрос...)'),
        ),
    ]
