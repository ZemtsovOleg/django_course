from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

week_days = ('monday', 'tuesday', 'wednesday',
             'thursday', 'friday', 'saturday', 'sunday')


def get_info(request):
    return render(request, 'week_days/greeting.html')


def get_info_about_singl_week_days_by_number(request, singl_week_days: int):
    days_name = week_days[singl_week_days-1]
    redirect_url_days = reverse('week_days_urls_name', args=(days_name, ))
    if singl_week_days in (1, 2, 3, 4, 5, 6, 7):
        return HttpResponseRedirect(redirect_url_days)
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {singl_week_days}')


def get_info_about_singl_week_days(request, singl_week_days: str):
    if singl_week_days in week_days:
        return HttpResponse(f'Список дел, запланированных на {singl_week_days}')
    else:
        return HttpResponseNotFound('Вы попали в будущее или прошлое')
