from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

week_days = ('monday', 'tuesday', 'wednesday',
             'thursday', 'friday', 'saturday', 'sunday')


def get_info_about_singl_week_days_by_number(request, singl_week_days: int):
    if singl_week_days in (1, 2, 3, 4, 5, 6, 7):
        return HttpResponseRedirect(f'/todo_week/{week_days[singl_week_days-1]}')
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {singl_week_days}')


def get_info_about_singl_week_days(request, singl_week_days: str):
    if singl_week_days in week_days:
        return HttpResponse(f'Список дел, запланированных на {singl_week_days}')
    else:
        return HttpResponseNotFound('Вы попали в будущее или прошлое')
