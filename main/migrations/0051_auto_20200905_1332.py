# Generated by Django 3.0.1 on 2020-09-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='slug',
            field=models.SlugField(default=1, verbose_name=models.CharField(max_length=10, verbose_name='Номер заказа')),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='budget',
            name='budget_tag',
            field=models.CharField(choices=[('Реклама', 'Реклама'), ('Закуп', 'Закуп'), ('Торговля', 'Торговля'), ('Заказы', 'Заказы'), ('Материалы', 'Материалы'), ('Раскрутка аккаунтов', 'Раскрутка аккаунтов')], default='null', max_length=50),
        ),
    ]
