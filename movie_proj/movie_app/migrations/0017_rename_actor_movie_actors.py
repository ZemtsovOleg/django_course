# Generated by Django 4.2.2 on 2023-07-08 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0016_alter_movie_actor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='actor',
            new_name='actors',
        ),
    ]