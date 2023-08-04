from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('profile-url', args=(self.slug, ))