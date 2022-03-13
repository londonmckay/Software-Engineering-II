# Generated by Django 4.0.2 on 2022-03-09 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_alter_submission_textbox'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='is_graded',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='points_received',
        ),
        migrations.AddField(
            model_name='submission',
            name='is_graded',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submission',
            name='points_received',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
