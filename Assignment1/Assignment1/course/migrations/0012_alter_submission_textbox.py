# Generated by Django 4.0.2 on 2022-02-24 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_alter_submission_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='textbox',
            field=models.TextField(blank=True, null=True),
        ),
    ]
