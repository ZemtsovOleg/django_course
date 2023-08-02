from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'user_authentication/register.html'
    success_url = reverse_lazy('home-url')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'user_authentication/login.html'
