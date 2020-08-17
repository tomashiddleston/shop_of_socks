# Generated by Django 3.0.1 on 2020-08-15 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_auto_20200815_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('new', 'Новый'), ('sogl', 'Согласовывается'), ('sobir', 'Собирается'), ('dost', 'Доставляется'), ('complete', 'Выполнен'), ('otmena', 'Отменен')], default='Новый', max_length=100, verbose_name='Статус заказа'),
        ),
    ]
