# Generated by Django 3.2.8 on 2024-08-08 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0005_auto_20240808_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='phone_title',
            field=models.CharField(default=1, max_length=255, verbose_name='Заголовок (телефон)'),
            preserve_default=False,
        ),
    ]
