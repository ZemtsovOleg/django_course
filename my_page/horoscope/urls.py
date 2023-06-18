from django.urls import path
from . import views


urlpatterns = [
    path('<int:singl_zodiac>', views.get_info_about_singl_zodiac_by_number),
    path('<str:singl_zodiac>', views.get_info_about_singl_zodiac),
]
