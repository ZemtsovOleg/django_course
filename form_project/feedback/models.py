from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.


class Feedback(models.Model):
    favorite_city = models.CharField(
        null=False, max_length=255, validators=[MinLengthValidator(3)])
    age = models.PositiveIntegerField(null=False, validators=[
        MinValueValidator(18), MaxValueValidator(120)])
    favorite_pizza = models.CharField(max_length=255, blank=True)
    feedback_two = models.TextField(blank=True)
