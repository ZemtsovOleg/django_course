from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(null=False)

    def save(self, *args, **kwargs):
        combined_name = f"{self.first_name} {self.last_name}"
        self.slug = slugify(combined_name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('director-url', args=(self.slug, ))


class Movie(models.Model):

    COUNTRIES_CHOICES = [
        ('US', 'USA'),
        ('CA', 'Canada'),
        ('JP', 'Japan'),
        ('AI', 'England')
    ]

    name = models.CharField(max_length=150)
    # director = models.ForeignKey(
    #     Director, on_delete=models.PROTECT, blank=True, null=True, default='')
    rating = models.IntegerField(blank=True, null=True, validators=[
                                 MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(blank=True, null=True, validators=[
        MinValueValidator(1895), MaxValueValidator(2050)])
    budget = models.IntegerField(
        blank=True, null=True, validators=[MinValueValidator(1)])
    country = models.CharField(
        max_length=2, choices=COUNTRIES_CHOICES, default='')
    slug = models.SlugField(null=False)

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='movie_name_index'),
        ]

    def get_url(self):
        return reverse('movie-url', args=(self.slug, ))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.id}, {self.name}'


# from movie_app.models import Movie
