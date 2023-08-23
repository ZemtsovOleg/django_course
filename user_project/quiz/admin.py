from django.contrib import admin

from .models import PossibleAnswer, Question, Survey, UserResponse

# Register your models here.


@admin.register(PossibleAnswer)
class PossibleAnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    filter_horizontal = ['options']


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    filter_horizontal = ['questions']


@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    pass