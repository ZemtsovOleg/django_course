from django.contrib import admin
from .models import Movie, Director, Actor

# Register your models here.


class BaseAdmin(admin.ModelAdmin):
    exclude = ['slug']
    list_per_page = 20


class PersonAdmin(BaseAdmin):
    list_display = ['id', 'first_name', 'last_name', 'slug']
    list_editable = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']


@admin.register(Director)
class DirectorAdmin(PersonAdmin):
    pass


@admin.register(Actor)
class ActorAdmin(PersonAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(BaseAdmin):
    list_display = ['id', 'name', 'director',
                    'rating', 'year', 'budget', 'country', 'is_published', 'slug']
    list_editable = ['name', 'director', 'rating', 'year', 'budget', 'country', 'is_published']
    search_fields = ['name', 'actors', 'director', 'year', 'country']
    list_filter = ['year', 'country']
    filter_horizontal = ['actors']
    # ordering = ['name']
