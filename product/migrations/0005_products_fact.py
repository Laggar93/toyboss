# Generated by Django 3.2.8 on 2024-07-16 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20240716_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='fact',
            field=models.TextField(blank=True, verbose_name='Факт'),
        ),
    ]
