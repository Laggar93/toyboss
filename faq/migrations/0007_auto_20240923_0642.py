# Generated by Django 3.2.8 on 2024-09-23 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0006_faqpage_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqpage',
            name='main_button',
            field=models.CharField(default=1, max_length=255, verbose_name='Все вопросы (кнопка на главной странице)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faqpage',
            name='main_button_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Все вопросы (кнопка на главной странице)'),
        ),
        migrations.AddField(
            model_name='faqpage',
            name='main_button_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Все вопросы (кнопка на главной странице)'),
        ),
        migrations.AddField(
            model_name='faqpage',
            name='main_button_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Все вопросы (кнопка на главной странице)'),
        ),
    ]
