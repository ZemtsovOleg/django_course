from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexListView.as_view(), name='home-url'),
    path('movies/', views.show_all_movies, name='movies-url'),
    path('directors/', views.show_all_directors, name='directors-url'),
    path('director/<slug:slug_director>',
         views.show_director, name='director-url'),
    path('actors/', views.ActorsListView.as_view(), name='actors-url'),
    path('actor/<slug:slug_actor>',
         views.ActorDetailView.as_view(), name='actor-url'),
    path('login/', views.LoginUserLoginView.as_view(), name='login-url'),
    path('register/', views.RegisterUserCreateView.as_view(), name='register-url'),
    path('<slug:slug_movie>', views.show_movie, name='movie-url'),
]
