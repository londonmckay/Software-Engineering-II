# Generated by Django 2.2 on 2022-02-09 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20220209_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime),
        ),
    ]
