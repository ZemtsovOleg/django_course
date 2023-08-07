from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


def validate_date_of_birth(date_of_birth):
    today = now()
    if (today.year - date_of_birth.year) < 18:
        raise ValidationError(
            _('You must be at least 18 years old to register.'))


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    slug = models.SlugField(unique=True)
    date_of_birth = models.DateField(validators=[
        validate_date_of_birth
    ])
    email_verify = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profile-url', args=(self.slug, ))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
