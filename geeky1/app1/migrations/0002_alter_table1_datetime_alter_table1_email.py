# Generated by Django 4.2.2 on 2023-06-30 07:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table1',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 30, 7, 55, 33, 697387, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='table1',
            name='email',
            field=models.EmailField(default='not available', max_length=254),
        ),
    ]