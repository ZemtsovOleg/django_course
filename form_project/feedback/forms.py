from django import forms

from .models import Feedback

# class FeedbackForm(forms.Form):
#     favorite_city = forms.CharField(label='Favorite city', min_length=2, max_length=255)
#     age = forms.IntegerField(label='Age', max_value=130, min_value=18)
#     favorite_pizza = forms.CharField(label='Favorite pizza', required=False)
#     feedback_two = forms.CharField(label='Feedback two', widget=forms.Textarea(), required=False)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        labels = {
            'favorite_city': 'Favorite city',
            'age': 'Age',
            'favorite_pizza': 'Favorite pizza',
            'feedback_two': 'Feedback two'
        }
