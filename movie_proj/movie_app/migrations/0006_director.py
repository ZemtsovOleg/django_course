# Generated by Django 4.2.2 on 2023-07-07 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_movie_country_alter_movie_budget_alter_movie_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
