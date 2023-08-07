from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView
from django.core.mail import send_mail

# from .utils import send_email_for_verify
from .forms import CustomUserCreationForm, FeedbackForm


class HomePageView(TemplateView):
    template_name = 'user/index.html'


class SignUpCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('confirm-email_url')

    # def post(self, request, *args, **kwargs): 
    #     result = super().post(request, *args, **kwargs)
    #     send_email_for_verify(self, request)
    #     return result


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'

    def form_valid(self, form):
        form_email = form.cleaned_data['email']
        CustomUser = get_user_model()

        try:
            CustomUser.objects.get(email=form_email)
        except ObjectDoesNotExist:
            form.add_error(
                'email', "This email does not exist in the database.")
            return self.form_invalid(form)

        return super().form_valid(form)


class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'
    login_url = reverse_lazy('login')


class FeedbackFormView(FormView):
    template_name = 'user/feedback.html'
    success_url = reverse_lazy('home-url')
    form_class = FeedbackForm


class ConfirmEmail(TemplateView):
    template_name = 'registration/confirm_email.html'
