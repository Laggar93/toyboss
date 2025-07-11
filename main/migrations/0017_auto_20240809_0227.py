# Generated by Django 3.2.8 on 2024-08-09 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_mainquote'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainquote',
            name='history_text',
            field=models.TextField(default=1, verbose_name='Текст истории'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainquote',
            name='history_text_en',
            field=models.TextField(null=True, verbose_name='Текст истории'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='history_text_ky',
            field=models.TextField(null=True, verbose_name='Текст истории'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='history_text_ru',
            field=models.TextField(null=True, verbose_name='Текст истории'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='history_title',
            field=models.CharField(default=1, max_length=255, verbose_name='Заголовок истории'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainquote',
            name='history_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок истории'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='history_title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок истории'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='history_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок истории'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='mission_text',
            field=models.TextField(default=1, verbose_name='Текст миссии'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainquote',
            name='mission_text_en',
            field=models.TextField(null=True, verbose_name='Текст миссии'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='mission_text_ky',
            field=models.TextField(null=True, verbose_name='Текст миссии'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='mission_text_ru',
            field=models.TextField(null=True, verbose_name='Текст миссии'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='mission_title',
            field=models.CharField(default=1, max_length=255, verbose_name='Заголовок миссии'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainquote',
            name='mission_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок миссии'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='mission_title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок миссии'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='mission_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок миссии'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='value_text',
            field=models.TextField(default=1, verbose_name='Текст ценности'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainquote',
            name='value_text_en',
            field=models.TextField(null=True, verbose_name='Текст ценности'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='value_text_ky',
            field=models.TextField(null=True, verbose_name='Текст ценности'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='value_text_ru',
            field=models.TextField(null=True, verbose_name='Текст ценности'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='value_title',
            field=models.CharField(default=1, max_length=255, verbose_name='Заголовок ценности'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainquote',
            name='value_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок ценности'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='value_title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок ценности'),
        ),
        migrations.AddField(
            model_name='mainquote',
            name='value_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок ценности'),
        ),
    ]
