from django.db.models import Avg, Count, Sum
# from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from django.db.models import Prefetch
from django.views.generic.edit import UpdateView

from .forms import MovieForm
from .models import Actor, Director, Movie

# Create your views here.


def show_all_movies(request):
    movies = Movie.objects.all().order_by('name')
    agg = movies.aggregate(Sum('budget'), Avg('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html',
                  {'movies': movies, 'agg': agg})


def show_all_directors(request):
    directors = Director.objects.all().order_by(
        'first_name', 'last_name').defer('gender', 'country')
    return render(request, 'movie_app/all_directors.html',
                  {'directors': directors})


def show_director(request, slug_director: str):
    director = get_object_or_404(Director.objects.defer(
        'gender', 'country', 'slug'), slug=slug_director)
    movies = Movie.objects.filter(director=director).only('name', 'slug')
    return render(request, 'movie_app/director.html', {'director': director, 'movies': movies})


class IndexListView(ListView):
    paginate_by = 7
    template_name = 'movie_app/index.html'
    model = Movie
    ordering = ['name']
    context_object_name = 'movies'  # object_list
    queryset = Movie.objects.filter(is_published=True).select_related(
        'director').prefetch_related('actors')


class ActorsListView(ListView):
    paginate_by = 4
    template_name = 'movie_app/all_actors.html'
    model = Actor
    context_object_name = 'actors'
    ordering = ['first_name', 'last_name']
    queryset = Actor.objects.defer('gender', 'country')


class ActorDetailView(DetailView):
    template_name = 'movie_app/actor.html'
    model = Actor
    slug_url_kwarg = 'slug_actor'
    queryset = Actor.objects.only('first_name', 'last_name').prefetch_related(
        Prefetch('movie_set', queryset=Movie.objects.only('name', 'slug')))


class MovieDetailView(DetailView):
    template_name = 'movie_app/movie.html'
    model = Movie
    slug_url_kwarg = 'slug_movie'
    queryset = Movie.objects.filter(is_published=True).select_related(
        'director').prefetch_related('actors')


class MovieUpdateView(UpdateView):
    template_name = 'movie_app/movie_update.html'
    model = Movie
    form_class = MovieForm
    success_url = 'home-url'
    slug_url_kwarg = 'slug_movie'


# def pageNotFound(request, exception):
#     return HttpResponseNotFound('Page not found')


# def show_actor(request, slug_actor: str):
#     actor = get_object_or_404(Actor, slug=slug_actor)
#     return render(request, 'movie_app/actor.html', {'actor': actor})


# def show_all_actors(request):
#     actors = Actor.objects.all().order_by('first_name', 'last_name')
#     return render(request, 'movie_app/all_actors.html',
#                   {'actors': actors})


# def show_movie(request, slug_movie: str):
#     movie = get_object_or_404(Movie, slug=slug_movie)
#     return render(request, 'movie_app/movie.html', {'movie': movie})
