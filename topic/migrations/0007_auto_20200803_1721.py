# Generated by Django 3.0.6 on 2020-08-03 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0006_dailypick_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pick',
            name='age_range',
        ),
        migrations.RemoveField(
            model_name='pick',
            name='gender',
        ),
    ]
