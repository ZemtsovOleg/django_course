from django.db.models import Avg, Count, F, Max, Min, Sum
from django.shortcuts import get_object_or_404, render

from .models import Movie

# Create your views here.


def show_all_movies(request):
    movies = Movie.objects.all().order_by('name')
    agg = movies.aggregate(Sum('budget'), Avg('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html',
                  {'movies': movies, 'agg': agg})


def show_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/movie.html', {'movie': movie})
