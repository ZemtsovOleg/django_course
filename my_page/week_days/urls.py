from django.urls import path
from . import views


urlpatterns = [
    path('<int:singl_week_days>/', views.get_info_about_singl_week_days_by_number),
    path('<str:singl_week_days>/', views.get_info_about_singl_week_days),
]
