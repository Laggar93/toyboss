# Generated by Django 3.2.8 on 2024-06-27 16:07

from django.db import migrations, models
import toyboss.functions


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20240627_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsslider',
            name='image_1499_jpg',
            field=models.ImageField(blank=True, upload_to=toyboss.functions.get_file_path),
        ),
        migrations.AddField(
            model_name='newsslider',
            name='image_1499_webp',
            field=models.ImageField(blank=True, upload_to=toyboss.functions.get_file_path),
        ),
    ]
