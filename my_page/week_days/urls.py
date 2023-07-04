from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_info),
    path('<int:singl_week_days>', views.get_info_about_singl_week_days_by_number),
    path('<str:singl_week_days>', views.get_info_about_singl_week_days,
         name='week_days_urls_name'),
]
