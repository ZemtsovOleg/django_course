from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page),
    path('posts/', views.posts),
    path('posts/<int:name_post>/', views.get_name_post_numbers),
    path('posts/<str:name_post>/', views.get_name_post),
]
