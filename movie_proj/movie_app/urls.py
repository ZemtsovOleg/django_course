from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_all_movies, name='home'),
    path('directors/', views.show_all_directors),
    path('director/<slug:slug_director>', views.show_director, name='director-url'),
    path('actors/', views.ActorsListView.as_view()),
    path('actor/<slug:slug_actor>', views.ActorDetailView.as_view(), name='actor-url'),
    # path('actor/<slug:slug_actor>', views.show_actor, name='actor-url'),
    path('<slug:slug_movie>', views.show_movie, name='movie-url'),
]

