# Generated by Django 5.0.1 on 2024-01-03 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='gmail',
            field=models.EmailField(default=1, max_length=254, verbose_name='Gmail'),
            preserve_default=False,
        ),
    ]
