# Generated by Django 5.1.4 on 2025-03-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0010_customcakeorder_berries_customcakeorder_cake_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customcakeorder',
            name='levels',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='Уровни'),
        ),
        migrations.AlterField(
            model_name='customcakeorder',
            name='topping',
            field=models.CharField(blank=True, default='none', max_length=20, null=True, verbose_name='Топпинг'),
        ),
    ]
