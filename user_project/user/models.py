from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_slug


validate_slug.message = _(
    "Enter a valid value consisting of letters, numbers, underscores, or hyphens.")


def validate_date_of_birth(date_of_birth):
    today = now()
    if (today.year - date_of_birth.year) < 18 or (today.year - date_of_birth.year) > 130:
        raise ValidationError(
            _('You must be at least 18 years old to register.'))


class CustomUser(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and -/_ only."
        ),
        validators=(validate_slug, ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
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
        return reverse_lazy('profile-url', args=(self.slug, ))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
