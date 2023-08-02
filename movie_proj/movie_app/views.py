from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.db.models import Avg, Count, F, Max, Min, Sum
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

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


class IndexListView(ListView):
    template_name = 'movie_app/index.html'
    model = Movie
    context_object_name = 'movies'  # object_list


class ActorsListView(ListView):
    paginate_by = 5
    template_name = 'movie_app/all_actors.html'
    model = Actor
    context_object_name = 'actors'

    def get_queryset(self):
        return Actor.objects.all().order_by('id')


class ActorDetailView(DetailView):
    template_name = 'movie_app/actor.html'
    model = Actor
    slug_url_kwarg = 'slug_actor'


class RegisterUserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'movie_app/register.html'
    success_url = reverse_lazy('home-url')


class LoginUserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'movie_app/login.html'
    success_url = reverse_lazy('home-url')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Page not found')


# def show_actor(request, slug_actor: str):
#     actor = get_object_or_404(Actor, slug=slug_actor)
#     return render(request, 'movie_app/actor.html', {'actor': actor})


# def show_all_actors(request):
#     actors = Actor.objects.all().order_by('first_name', 'last_name')
#     return render(request, 'movie_app/all_actors.html',
#                   {'actors': actors})
