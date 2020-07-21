# Generated by Django 3.0.6 on 2020-07-16 13:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0002_dailypick'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick',
            name='selection',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
    ]
