from django.views.generic.list import ListView


from .models import Question

# Create your views here.


class SurveyPageView(ListView):
    model = Question
    template_name = 'quiz/survey.html'
    context_object_name = 'questions'
    # queryset = Question.objects.filter(tattoo=True)
