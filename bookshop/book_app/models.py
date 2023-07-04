from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField()
    author = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f'{self.title}, {self.rating}, {self.is_best_selling}, {self.author}'

# from book_app.models import Book