# Generated by Django 4.2.2 on 2023-07-08 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0014_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(blank=True, null=True, to='movie_app.actor'),
        ),
    ]
