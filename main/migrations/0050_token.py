# Generated by Django 3.0.1 on 2020-08-30 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0049_auto_20200830_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=100, verbose_name='Токен доступа')),
            ],
        ),
    ]