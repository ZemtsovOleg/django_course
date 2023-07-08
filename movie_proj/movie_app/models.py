from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class CountryMixin(models.Model):
    COUNTRIES_CHOICES = (
        ('US', 'USA'),
        ('CA', 'Canada'),
        ('JP', 'Japan'),
        ('AI', 'England')
    )

    country = models.CharField(
        max_length=2, blank=True, choices=COUNTRIES_CHOICES, default='')

    class Meta:
        abstract = True


class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    slug = models.SlugField(null=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.get_full_name())
        return super().save(*args, **kwargs)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()


class Director(CountryMixin, Person):

    def get_url(self):
        return reverse('director-url', args=(self.slug, ))


class Actor(CountryMixin, Person):

    def get_url(self):
        return reverse('actor-url', args=(self.slug, ))


class Movie(CountryMixin, models.Model):
    name = models.CharField(max_length=150)
    # director = models.ForeignKey(
    #     Director, on_delete=models.PROTECT, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True, validators=[
                                 MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(blank=True, null=True, validators=[
        MinValueValidator(1895), MaxValueValidator(2050)])
    budget = models.IntegerField(
        blank=True, null=True, validators=[MinValueValidator(1)])
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