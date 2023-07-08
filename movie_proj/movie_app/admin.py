from django.contrib import admin
from .models import Movie#, Director

# Register your models here.


# class DirectorAdmin(admin.ModelAdmin):
#     exclude = ['slug']
#     list_display = ['id', 'first_name', 'last_name', 'slug']
#     list_per_page = 20
#     list_editable = ['first_name', 'last_name']
#     search_fields = ['first_name', 'last_name']


class MovieAdmin(admin.ModelAdmin):
    exclude = ['slug']
    list_display = ['id', 'name',
                    'rating', 'year', 'budget', 'country', 'slug']
    list_per_page = 20
    list_editable = ['name', 'rating', 'year', 'budget', 'country']
    search_fields = ['name', 'year', 'country']
    list_filter = ['year', 'country']


admin.site.register(Movie, MovieAdmin)
# admin.site.register(Director, DirectorAdmin)
