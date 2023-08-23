import uuid
from typing import Any

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView

from quiz.models import Survey

from .forms import CustomUserCreationForm, FeedbackForm

CustomUser = get_user_model()


class HomePageView(TemplateView):
    template_name = 'user/index.html'


class SignUpCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('confirm-email-url')

    def form_valid(self, form):
        '''Sending an email for email verification '''
        token = uuid.uuid4().hex
        confirm_link = self.request.build_absolute_uri(
            reverse_lazy('email-confirmed-url', kwargs={'token': token}))
        email_body = f'Please use the link to complete registration: {confirm_link}'
        email = EmailMessage(
            subject='Confirm Your Email Address',
            body=email_body,
            to=(form.cleaned_data['email'], )
        )
        email.send()
        return super().form_valid(form)


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'

    def form_valid(self, form):
        '''Check if email is available in the database'''
        form_email = form.cleaned_data['email']

        try:
            CustomUser.objects.get(email=form_email)
        except ObjectDoesNotExist:
            form.add_error(
                'email', "This email does not exist in the database.")
            return self.form_invalid(form)

        return super().form_valid(form)


class ProfilePageView(LoginRequiredMixin, ListView):
    template_name = 'user/profile.html'
    login_url = reverse_lazy('login')
    model = Survey
    context_object_name = 'surveys'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        slug_user = self.kwargs['slug_user']
        get_object_or_404(CustomUser, slug=slug_user)
        return super().get(request, *args, **kwargs)


class FeedbackFormView(FormView):
    template_name = 'user/feedback.html'
    success_url = reverse_lazy('home-url')
    form_class = FeedbackForm


class ConfirmEmail(TemplateView):
    template_name = 'registration/confirm_email.html'


class ConfirmedEmail(TemplateView):
    template_name = 'registration/email_confirmed.html'
