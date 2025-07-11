# Generated by Django 3.2.8 on 2024-06-26 18:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_alter_points_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='advantages',
            name='fifth_advantage_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Пятое преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='fifth_advantage_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Пятое преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='fifth_advantage_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Пятое преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='first_advantage_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Первое преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='first_advantage_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Первое преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='first_advantage_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Первое преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='fourth_advantage_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Четвертое преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='fourth_advantage_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Четвертое преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='fourth_advantage_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Четвертое преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='main_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='main_title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='main_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='second_advantage_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Второе преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='second_advantage_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Второе преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='second_advantage_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Второе преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='sixth_advantage_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Шестое преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='sixth_advantage_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Шестое преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='sixth_advantage_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Шестое преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='third_advantage_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Третье преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='third_advantage_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Третье преимущество'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='third_advantage_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Третье преимущество'),
        ),
        migrations.AddField(
            model_name='points',
            name='point_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='points',
            name='point_title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='points',
            name='point_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='points',
            name='text_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='points',
            name='text_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='points',
            name='text_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='productionpage',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание SEO'),
        ),
        migrations.AddField(
            model_name='productionpage',
            name='description_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Описание SEO'),
        ),
        migrations.AddField(
            model_name='productionpage',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание SEO'),
        ),
        migrations.AddField(
            model_name='productionpage',
            name='keywords_en',
            field=models.TextField(blank=True, null=True, verbose_name='Ключевые слова SEO'),
        ),
        migrations.AddField(
            model_name='productionpage',
            name='keywords_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Ключевые слова SEO'),
        ),
        migrations.AddField(
            model_name='productionpage',
            name='keywords_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Ключевые слова SEO'),
        ),
        migrations.AddField(
            model_name='productionpage',
            name='page_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='productionpage',
            name='page_title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='productionpage',
            name='page_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='productionpage',
            name='title_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок SEO'),
        ),
        migrations.AddField(
            model_name='productionpage',
            name='title_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок SEO'),
        ),
        migrations.AddField(
            model_name='productionpage',
            name='title_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок SEO'),
        ),
    ]
