from django.core.validators import (MaxValueValidator, MinLengthValidator,
                                    MinValueValidator)
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Feedback(models.Model):
    full_name = models.CharField(
        max_length=255, unique=True, null=False, blank=False, validators=[MinLengthValidator(3)])
    age = models.PositiveIntegerField(null=False, validators=[
        MinValueValidator(18), MaxValueValidator(120)])
    favorite_city = models.CharField(
        max_length=255, validators=[MinLengthValidator(3)])
    favorite_pizza = models.CharField(max_length=255, blank=True)
    feedback_two = models.TextField(blank=True)
    tattoo = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, null=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.full_name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('full-name-url', args=(self.slug, ))
