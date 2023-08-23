from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from user.models import CustomUser

# Create your models here.


class PossibleAnswer(models.Model):
    option = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f'{self.option}'


class Question(models.Model):
    question = models.CharField(max_length=250)
    options = models.ManyToManyField(PossibleAnswer)

    def __str__(self) -> str:
        return f'{self.question}'


class Survey(models.Model):
    title = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)
    slug = models.SlugField(max_length=255, null=False, unique=True)

    def __str__(self) -> str:
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('survey-url', args=(self.slug, ))
    

class UserResponse(models.Model):
    id_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, default=None)
    id_question = models.ForeignKey(
        Question, on_delete=models.CASCADE, default=None)
    id_selected_answer = models.ForeignKey(
        PossibleAnswer, on_delete=models.CASCADE, default=None)
    id_survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, default=None)
