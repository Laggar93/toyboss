# Generated by Django 3.2.8 on 2024-07-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0024_remove_contactform_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='main_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Работа в Тойбосс'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='main_title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Работа в Тойбосс'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='main_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Работа в Тойбосс'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='message_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Ваше сообщение'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='message_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Ваше сообщение'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='message_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Ваше сообщение'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Ваше имя'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='name_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Ваше имя'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Ваше имя'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='phone_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Ваш номер'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='phone_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Ваш номер'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='phone_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Ваш номер'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='send_button_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Кнопка "Отправить"'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='send_button_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Кнопка "Отправить"'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='send_button_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Кнопка "Отправить"'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='subtitle_en',
            field=models.TextField(null=True, verbose_name='Подзаголовок (Хотите расти вместе с нами...)'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='subtitle_ky',
            field=models.TextField(null=True, verbose_name='Подзаголовок (Хотите расти вместе с нами...)'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='subtitle_ru',
            field=models.TextField(null=True, verbose_name='Подзаголовок (Хотите расти вместе с нами...)'),
        ),
    ]
