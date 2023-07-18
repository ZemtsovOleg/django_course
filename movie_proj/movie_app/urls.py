from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_all_movies, name='home'),
    path('directors/', views.show_all_directors),
    path('director/<slug:slug_director>', views.show_director, name='director-url'),
    path('actors/', views.show_all_actors),
    path('actor/<slug:slug_actor>', views.show_actor, name='actor-url'),
    path('<slug:slug_movie>', views.show_movie, name='movie-url'),
]
