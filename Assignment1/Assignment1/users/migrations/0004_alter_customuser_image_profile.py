# Generated by Django 4.0.2 on 2022-02-24 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_image_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image_profile',
            field=models.ImageField(blank=True, default='', max_length=1000, upload_to='profile_pics/'),
        ),
    ]
