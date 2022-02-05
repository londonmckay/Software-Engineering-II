# Generated by Django 2.2 on 2022-02-04 23:30

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20220204_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='user',
            field=models.OneToOneField(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
