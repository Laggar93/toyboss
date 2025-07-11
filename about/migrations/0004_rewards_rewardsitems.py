# Generated by Django 3.2.8 on 2024-06-25 10:37

from django.db import migrations, models
import django.db.models.deletion
import toyboss.functions


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_certificates_certificatesitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rewards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('button_name', models.CharField(max_length=255, verbose_name='Название кнопки')),
            ],
            options={
                'verbose_name': 'Награда',
                'verbose_name_plural': 'Награды',
            },
        ),
        migrations.CreateModel(
            name='RewardsItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward_image', models.ImageField(help_text='Формат файла: JPG, JPEG, PNG или WEBP. Ограничение размера: 3 Мбайт.', upload_to=toyboss.functions.get_file_path, verbose_name='Награда')),
                ('rewards', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewards_images', to='about.rewards')),
            ],
            options={
                'verbose_name': 'Изображение награды',
                'verbose_name_plural': 'Изображения награды',
            },
        ),
    ]
