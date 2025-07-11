# Generated by Django 3.2.8 on 2024-06-15 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketingDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marketing_department_title', models.CharField(max_length=255, verbose_name='Отдел маркетинга')),
                ('marketing_department_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('marketing_department_phone', models.CharField(max_length=255, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Отдел маркетинга',
                'verbose_name_plural': 'Отдел маркетинга',
            },
        ),
    ]
