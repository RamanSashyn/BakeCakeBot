# Generated by Django 5.1.4 on 2025-03-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_berry_decor_level_orderstatistics_shape_topping_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardcake',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True, verbose_name='Название торта'),
        ),
    ]
