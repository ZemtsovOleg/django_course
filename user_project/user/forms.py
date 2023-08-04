from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = super().clean_username()
        if username is None:
            return None
        # Здесь перечислите недопустимые значения слагов
        reserved_slugs = ('admin', 'user', 'profile', 'id', 'login')
        if username.lower() in reserved_slugs:
            raise ValidationError("This username is not allowed.")
        return username
