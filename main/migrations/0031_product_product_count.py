# Generated by Django 3.0.1 on 2020-07-21 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_product_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_count',
            field=models.CharField(default=999, max_length=3, verbose_name='Доступность'),
            preserve_default=False,
        ),
    ]
