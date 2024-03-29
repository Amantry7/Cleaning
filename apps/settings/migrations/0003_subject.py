# Generated by Django 5.0.1 on 2024-01-03 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_settings_gmail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=244, verbose_name='название')),
                ('image', models.ImageField(upload_to='subject/', verbose_name='фото')),
                ('image2', models.ImageField(upload_to='subject/', verbose_name='фото')),
                ('price', models.CharField(max_length=244, verbose_name='цена')),
                ('time', models.CharField(max_length=255, verbose_name='время')),
                ('disk', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Услага',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
