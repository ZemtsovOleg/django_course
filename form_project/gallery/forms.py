from django.forms import forms

from .models import Gallery

class GalleryUploadForm(forms.Form):
    image = forms.FileField()
