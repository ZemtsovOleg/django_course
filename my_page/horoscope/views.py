from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.


zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - <i>пятый знак зодиака</i>, солнце (с 23 июля по 21 августа).',
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


def get_info_about_singl_zodiac_by_number(request, singl_zodiac: int):
    if singl_zodiac in zodiac_dict_by_index:
        return HttpResponseRedirect(f'/horoscope/{zodiac_dict_by_index[singl_zodiac]}')
    else:
        return HttpResponseNotFound(f'Страницы {singl_zodiac} нет')


def get_info_about_singl_zodiac(request, singl_zodiac: str):
    if singl_zodiac in zodiac_dict:
        return HttpResponse(zodiac_dict[singl_zodiac])
    else:
        return HttpResponseNotFound(f'Страницы {singl_zodiac} тут нет')
