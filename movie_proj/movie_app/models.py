from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(null=True)
    slug = models.SlugField(default='', null=False)

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
        return f'{self.name}, {self.rating}, {self.year}, {self.budget}'


# from movie_app.models import Movie