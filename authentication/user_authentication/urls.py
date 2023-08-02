from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='user_authentication/index.html'), name='home-url'),
    path('login/', views.LoginUser.as_view(), name='login-url'),
    path('register/', views.RegisterUser.as_view(), name='register-url'),
]
