# Generated by Django 3.0.1 on 2020-08-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_name', models.CharField(max_length=100, verbose_name='На что?')),
                ('earn', models.FloatField(verbose_name='Доход/Расход')),
            ],
            options={
                'verbose_name': 'Бюджет',
                'verbose_name_plural': 'Бюджет',
            },
        ),
    ]
