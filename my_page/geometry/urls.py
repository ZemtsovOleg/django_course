from django.urls import path
from . import views


urlpatterns = [
    path('get_rectangle_area/<int:width>/<int:height>/',
         views.get_rectangle_area_redirect),
    path('get_square_area/<int:width>/', views.get_square_area_redirect),
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area),
    path('square/<int:width>/', views.get_square_area),
]
