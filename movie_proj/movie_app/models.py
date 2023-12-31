from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class AbstractCountryMixin(models.Model):
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


class AbstractPerson(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    slug = models.SlugField(max_length=255, null=False, unique=True)

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['name'], name='movie_name_idx'),
            models.Index(fields=['slug'], name='slug_idx'),
        ]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.get_full_name())
        return super().save(*args, **kwargs)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()


class Director(AbstractCountryMixin, AbstractPerson):

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['first_name', 'last_name'], name='unique_director')
        ]

    def get_absolute_url(self):
        return reverse('director-url', args=(self.slug, ))


class Actor(AbstractCountryMixin, AbstractPerson):

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['first_name', 'last_name'], name='unique_actor')
        ]

    def get_absolute_url(self):
        return reverse('actor-url', args=(self.slug, ))


class Movie(AbstractCountryMixin, models.Model):
    name = models.CharField(max_length=150, blank=False)
    director = models.ForeignKey(
        Director, on_delete=models.PROTECT, blank=True, null=True)
    actors = models.ManyToManyField(Actor, blank=True)
    rating = models.IntegerField(blank=True, null=True, validators=[
                                 MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(blank=True, null=True, validators=[
        MinValueValidator(1895), MaxValueValidator(2050)])
    premiere_date = models.DateField(null=True, blank=True)
    budget = models.IntegerField(
        blank=True, null=True, validators=[MinValueValidator(1)])
    color = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='movie_name_idx'),
            models.Index(fields=['slug'], name='slug_idx'),
        ]

    def get_absolute_url(self):
        return reverse('movie-url', args=(self.slug, ))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.id}, {self.name}'


# from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
# from movie_app.models import Movie, Director, Actor
# from django.db import connection
# python3 manage.py shell_plus
