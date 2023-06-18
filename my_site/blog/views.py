from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def main_page(request):
    return HttpResponse('Главная страница')


def posts(request):
    return HttpResponse('Все посты блога')


def get_name_post_numbers(request, name_post):
    return HttpResponse(f'Здесь содержится информация о посте под номером {name_post}')


def get_name_post(request, name_post):
    return HttpResponse(f'Информация о посте {name_post}')
