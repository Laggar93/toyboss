# Generated by Django 3.2.8 on 2024-07-17 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20240717_0410'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainpageslider',
            options={'ordering': ['order'], 'verbose_name': 'Главный слайдер', 'verbose_name_plural': 'Главный слайдер'},
        ),
        migrations.AddField(
            model_name='mainpageslider',
            name='order',
            field=models.IntegerField(default=1, verbose_name='Порядок'),
            preserve_default=False,
        ),
    ]
