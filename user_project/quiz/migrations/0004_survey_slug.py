# Generated by Django 4.2.2 on 2023-08-20 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_remove_userresponse_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='slug',
            field=models.SlugField(max_length=255, null=True),
        ),
    ]