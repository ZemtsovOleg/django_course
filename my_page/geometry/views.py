from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def square(request):
    return render(request, 'geometry/square.html')

def rectangle(request):
    return render(request, 'geometry/rectangle.html')

def circle(request):
    return render(request, 'geometry/circle.html')


def get_rectangle_area_redirect(request, width: int, height: int):
    redirect_url_rectangle = reverse('rectangle_urls_name', args=(width, height))
    return HttpResponseRedirect(redirect_url_rectangle)


def get_square_area_redirect(request, width: int):
    redirect_url_square = reverse('square_urls_name', args=(width, ))
    return HttpResponseRedirect(redirect_url_square)


def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f'Площадь прямоугольника размером {width}*{height} равен {width * height}')


def get_square_area(request, width: int):
    return HttpResponse(f'Площадь квадрата размером {width}*{width} равен {width * width}')


# def get_circle_area(request, singl_rectangle: int):
#     pass
