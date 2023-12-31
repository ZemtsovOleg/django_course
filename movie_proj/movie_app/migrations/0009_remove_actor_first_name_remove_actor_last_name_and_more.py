# Generated by Django 4.2.2 on 2023-07-08 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0008_movie_director'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='slug',
        ),
        migrations.AddField(
            model_name='director',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
