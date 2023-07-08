# Generated by Django 4.2.2 on 2023-07-08 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0012_delete_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, choices=[('US', 'USA'), ('CA', 'Canada'), ('JP', 'Japan'), ('AI', 'England')], default='', max_length=2)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('slug', models.SlugField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, choices=[('US', 'USA'), ('CA', 'Canada'), ('JP', 'Japan'), ('AI', 'England')], default='', max_length=2)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('slug', models.SlugField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]