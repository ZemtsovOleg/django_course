from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
import datetime

# Create your views here.


def is_valid_date(year, month, day):
    try:
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False


zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}


zodiac_dict_by_index = {
    1: 'aries',
    2: 'taurus',
    3: 'gemini',
    4: 'cancer',
    5: 'leo',
    6: 'virgo',
    7: 'libra',
    8: 'scorpio',
    9: 'sagittarius',
    10: 'capricorn',
    11: 'aquarius',
    12: 'pisces',
}


zodiac_element = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def type_horoscope(request):
    li_elements = ''
    for sign in zodiac_element:
        redirect_path = reverse('horoscope-urls-name', args=(sign, ))
        li_elements += f"<li> <a href='{redirect_path}'> {sign.title()} </a> </li>"
    return HttpResponse(f'<ol>{li_elements}</ol>')


def get_info_about_type_zodiac(request, type_zodiac):
    li_elements = ''
    for sign in zodiac_element[type_zodiac]:
        redirect_path = reverse('horoscope-urls-name', args=(sign, ))
        li_elements += f"<li> <a href='{redirect_path}'> {sign.title()} </a> </li>"
    return HttpResponse(f'<ol>{li_elements}</ol>')


def get_info_about_singl_zodiac_by_number(request, singl_zodiac: int):
    zodiac_name = zodiac_dict_by_index[singl_zodiac]
    redirect_url_horoscope = reverse(
        'horoscope-urls-name', args=(zodiac_name, ))
    if singl_zodiac in zodiac_dict_by_index:
        return HttpResponseRedirect(redirect_url_horoscope)
    else:
        return HttpResponseNotFound(f'Страницы {singl_zodiac} нет')


def get_info_month_day(request, month, day):
    if is_valid_date(2023, month, day):
        return HttpResponse((month, day))
    else:
        return HttpResponseNotFound(f'Страницы {month, day} тут нет')


def get_info_about_singl_zodiac(request, singl_zodiac: str):
    if singl_zodiac in zodiac_dict:
        context = {
            'description': zodiac_dict[singl_zodiac],
            'zodiac_dict': zodiac_dict,
        }
        return render(request, 'horoscope/info_zodiac.html', context=context)
    else:
        return HttpResponseNotFound(f'Страницы {singl_zodiac} тут нет')


def index(request):
    context = {
        'zodiac_dict': zodiac_dict,
    }
    return render(request, 'horoscope/index.html', context=context)
