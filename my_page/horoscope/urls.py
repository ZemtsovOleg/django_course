from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='horoscope-urls-index'),
    path('type', views.type_horoscope),
    path('type/<str:type_zodiac>', views.get_info_about_type_zodiac,
         name='horoscope_urls_type'),
    path('<int:month>/<int:day>', views.get_info_month_day),
    path('<int:singl_zodiac>', views.get_info_about_singl_zodiac_by_number),
    path('<str:singl_zodiac>', views.get_info_about_singl_zodiac,
         name='horoscope-urls-name'),
]
