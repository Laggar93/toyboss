# Generated by Django 3.2.8 on 2024-06-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_title', models.CharField(max_length=255, verbose_name='График работы')),
                ('monday_friday', models.CharField(max_length=255, verbose_name='Понедельник - пятницы')),
                ('saturday', models.CharField(max_length=255, verbose_name='Суббота')),
                ('dinner', models.CharField(max_length=255, verbose_name='Обед')),
            ],
            options={
                'verbose_name': 'График работы',
                'verbose_name_plural': 'График работы',
            },
        ),
    ]
