# Generated by Django 3.0.1 on 2020-08-04 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='Новый', max_length=100, verbose_name='Статус заказа'),
        ),
    ]
