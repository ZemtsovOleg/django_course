# Generated by Django 4.2.2 on 2023-08-20 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0002_userresponse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresponse',
            name='question',
        ),
        migrations.RemoveField(
            model_name='userresponse',
            name='selected_answer',
        ),
        migrations.RemoveField(
            model_name='userresponse',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='userresponse',
            name='user',
        ),
        migrations.AddField(
            model_name='userresponse',
            name='id_question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='quiz.question'),
        ),
        migrations.AddField(
            model_name='userresponse',
            name='id_selected_answer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='quiz.possibleanswer'),
        ),
        migrations.AddField(
            model_name='userresponse',
            name='id_survey',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='quiz.survey'),
        ),
        migrations.AddField(
            model_name='userresponse',
            name='id_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
