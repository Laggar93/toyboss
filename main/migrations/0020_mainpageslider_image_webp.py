# Generated by Django 3.2.8 on 2025-02-22 11:02

from django.db import migrations, models
import toyboss.functions


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_mainquote_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpageslider',
            name='image_webp',
            field=models.ImageField(default=1, upload_to=toyboss.functions.get_file_path),
            preserve_default=False,
        ),
    ]
