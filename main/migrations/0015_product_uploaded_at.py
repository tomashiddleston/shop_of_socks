# Generated by Django 3.0.1 on 2020-07-21 16:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200721_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
