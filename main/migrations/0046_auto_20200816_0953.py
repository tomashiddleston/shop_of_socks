# Generated by Django 3.0.1 on 2020-08-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_auto_20200815_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(max_length=100, verbose_name='Статус заказа'),
        ),
    ]
