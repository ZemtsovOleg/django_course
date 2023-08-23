from django import forms

from .models import UserResponse


class UserResponseForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ('id_user', 'id_question', 'id_selected_answer', 'id_survey')

        # labels = {
        #     'favorite_city': 'Favorite city',
        #     'age': 'Age',
        #     'favorite_pizza': 'Favorite pizza',
        #     'feedback_two': 'Feedback two'
        # }
        # fields = ('username', 'date_of_birth',
        #           'email', 'password1', 'password2')
        # widgets = {
        #     'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        # }
