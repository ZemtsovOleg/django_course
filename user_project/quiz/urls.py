from django.urls import path

from .views import SurveyPageView

urlpatterns = [
    path('<slug:slug_survey>/', SurveyPageView.as_view(), name='survey-url'),
]
