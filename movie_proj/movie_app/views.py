from django.db.models import Avg, Count, F, Max, Min, Sum
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from .models import Actor, Director, Movie

# Create your views here.


def show_all_movies(request):
    movies = Movie.objects.all().order_by('name')
    agg = movies.aggregate(Sum('budget'), Avg('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html',
                  {'movies': movies, 'agg': agg})


def show_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/movie.html', {'movie': movie})


def show_all_directors(request):
    directors = Director.objects.all().order_by('first_name', 'last_name')
    return render(request, 'movie_app/all_directors.html',
                  {'directors': directors})


def show_director(request, slug_director: str):
    director = get_object_or_404(Director, slug=slug_director)
    return render(request, 'movie_app/director.html', {'director': director})


# def show_all_actors(request):
#     actors = Actor.objects.all().order_by('first_name', 'last_name')
#     return render(request, 'movie_app/all_actors.html',
#                   {'actors': actors})


class ActorsListView(ListView):
    template_name = 'movie_app/all_actors.html'
    model = Actor
    context_object_name = 'actors'  # object_list


# def show_actor(request, slug_actor: str):
#     actor = get_object_or_404(Actor, slug=slug_actor)
#     return render(request, 'movie_app/actor.html', {'actor': actor})

class ActorDetailView(DetailView):
    template_name = 'movie_app/actor.html'
    model = Actor
    slug_url_kwarg = 'slug_actor'
