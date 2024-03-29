# Generated by Django 5.0.1 on 2024-01-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='имя')),
                ('phone', models.CharField(max_length=255, verbose_name='номер телефона')),
                ('email', models.CharField(max_length=255, verbose_name='почта')),
                ('sabject', models.CharField(max_length=255, verbose_name='услуга')),
                ('message', models.TextField(verbose_name='cообщение')),
            ],
            options={
                'verbose_name': 'запрос на связь',
                'verbose_name_plural': 'запросы на связи',
            },
        ),
    ]
