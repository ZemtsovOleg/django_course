from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_all_movies),
    # path('directors/', views.show_all_directors),
    # path('directors/<slug:slug_director>', views.show_director, name='director-url'),
    path('<slug:slug_movie>', views.show_movie, name='movie-url'),
]
