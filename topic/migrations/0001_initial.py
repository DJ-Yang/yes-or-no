# Generated by Django 3.0.6 on 2020-05-31 13:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('thumb_image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('author', models.CharField(default='admin', max_length=100)),
                ('selection1_image', models.ImageField(upload_to='')),
                ('selection1_des', models.CharField(max_length=20)),
                ('selection2_image', models.ImageField(upload_to='')),
                ('selection2_des', models.CharField(max_length=20)),
                ('hot_topic', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select', models.IntegerField(blank=True, choices=[(0, 'Yes'), (1, 'No')], null=True)),
                ('age_range', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('selector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.Topic')),
            ],
        ),
    ]
