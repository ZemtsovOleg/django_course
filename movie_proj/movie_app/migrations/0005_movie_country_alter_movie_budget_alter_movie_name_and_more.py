# Generated by Django 4.2.2 on 2023-07-07 21:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_movie_movie_name_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.CharField(choices=[('US', 'USA'), ('CA', 'Canada'), ('JP', 'Japan'), ('AI', 'England')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1895), django.core.validators.MaxValueValidator(2050)]),
        ),
    ]