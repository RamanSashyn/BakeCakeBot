# Generated by Django 5.1.4 on 2025-03-05 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_alter_customcake_topping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cakeorder',
            name='telegram_id',
        ),
    ]
