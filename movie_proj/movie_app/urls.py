from django.urls import path

from . import views

# app_name = 'movie_app' "{% url 'movie_app:home-url' %}"
# namespace

urlpatterns = [
    path('', views.IndexListView.as_view(), name='home-url'),
    path('movies/', views.show_all_movies, name='movies-url'),
    path('actors/', views.ActorsListView.as_view(), name='actors-url'),
    path('directors/', views.show_all_directors, name='directors-url'),
    path('director/<slug:slug_director>',
         views.show_director, name='director-url'),
    path('actor/<slug:slug_actor>',
         views.ActorDetailView.as_view(), name='actor-url'),
    path('<slug:slug_movie>', views.MovieDetailView.as_view(), name='movie-url'),
    path('update-movie/<slug:slug_movie>',
         views.MovieUpdateView.as_view(), name='update-movie')
]
