# Generated by Django 4.1.6 on 2023-07-03 12:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_table2_alter_table1_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='table3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='table1',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 12, 10, 29, 801411, tzinfo=datetime.timezone.utc)),
        ),
    ]
