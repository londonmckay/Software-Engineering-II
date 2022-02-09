# Generated by Django 2.2 on 2022-02-09 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='card_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='cvc_number',
        ),
        migrations.RemoveField(
            model_name='account',
            name='expire_date',
        ),
        migrations.AddField(
            model_name='account',
            name='cardholder_name',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='cvv_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='expiration_date',
            field=models.DateField(default=datetime.date, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='card_number',
            field=models.IntegerField(null=True),
        ),
    ]
