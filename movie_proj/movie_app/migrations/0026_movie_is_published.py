# Generated by Django 4.2.2 on 2023-08-05 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0025_movie_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
