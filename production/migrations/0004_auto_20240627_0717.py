# Generated by Django 3.2.8 on 2024-06-27 07:17

from django.db import migrations, models
import toyboss.functions


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0003_auto_20240626_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointsslider',
            name='image_735_jpg',
            field=models.ImageField(blank=True, upload_to=toyboss.functions.get_file_path),
        ),
        migrations.AddField(
            model_name='pointsslider',
            name='image_735_webp',
            field=models.ImageField(blank=True, upload_to=toyboss.functions.get_file_path),
        ),
    ]
