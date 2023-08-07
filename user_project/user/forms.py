from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'date_of_birth',
                  'email', 'password1', 'password2')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_username(self):
        username = super().clean_username()
        if username is None:
            return None
        # Здесь перечислите недопустимые значения слагов
        reserved_slugs = ('admin', 'user', 'profile', 'id', 'login', 'password_reset')
        if username.lower() in reserved_slugs:
            raise ValidationError("This username is not allowed.")
        return username


class FeedbackForm(forms.Form):
    full_name = forms.CharField(
        label='Full name', min_length=2, max_length=255)
    email = forms.EmailField(label='email')
    feedback = forms.CharField(
        label='Feedback', widget=forms.Textarea(), min_length=6)
