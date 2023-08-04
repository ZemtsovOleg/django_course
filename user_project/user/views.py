from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.shortcuts import redirect

from .forms import CustomUserCreationForm

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'user/index.html'


class SignUpCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'


class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'
    login_url = reverse_lazy('login')

'''Рекомендуется реализовать ограничение числа попыток входа и блокировку учетных записей после нескольких неудачных попыток.'''
