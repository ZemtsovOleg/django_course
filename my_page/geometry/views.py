from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.


def get_rectangle_area_redirect(request, width: int, height: int):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')


def get_square_area_redirect(request, width: int):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}')


def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f'Площадь прямоугольника размером {width}*{height} равен {width * height}')


def get_square_area(request, width: int):
    return HttpResponse(f'Площадь квадрата размером {width}*{width} равен {width * width}')


# def get_circle_area(request, singl_rectangle: int):
#     pass
