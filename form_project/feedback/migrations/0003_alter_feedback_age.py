# Generated by Django 4.2.2 on 2023-07-22 18:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_feedback_favorite_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='age',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(120)]),
        ),
    ]
