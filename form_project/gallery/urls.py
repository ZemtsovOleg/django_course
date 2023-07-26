from django.urls import path

from . import views

urlpatterns = [
    path('load_file', views.GalleryCreateView.as_view()),
    path('list_file', views.GalleryListView.as_view()),
]
