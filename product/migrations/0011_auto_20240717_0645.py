# Generated by Django 3.2.8 on 2024-07-17 06:45

from django.db import migrations, models
import toyboss.functions


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='first_image_animation',
            field=models.ImageField(blank=True, help_text='Формат файла: JPG, JPEG, PNG или WEBP. Ограничение размера: 3 Мбайт.', upload_to=toyboss.functions.get_file_path, verbose_name='Первое изображение анимации'),
        ),
        migrations.AddField(
            model_name='products',
            name='second_image_animation',
            field=models.ImageField(blank=True, help_text='Формат файла: JPG, JPEG, PNG или WEBP. Ограничение размера: 3 Мбайт.', upload_to=toyboss.functions.get_file_path, verbose_name='Второе изображение анимации'),
        ),
        migrations.AddField(
            model_name='products',
            name='third_image_animation',
            field=models.ImageField(blank=True, help_text='Формат файла: JPG, JPEG, PNG или WEBP. Ограничение размера: 3 Мбайт.', upload_to=toyboss.functions.get_file_path, verbose_name='Третье изображение анимации'),
        ),
    ]
