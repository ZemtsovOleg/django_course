from django.urls import path

from .views import FeedBackListView, DoneTemplateView, FeedbackUpdateView, FeedbackCreateView, FeedBackDetailView

urlpatterns = [
    path('', FeedbackCreateView.as_view()),
    path('done', DoneTemplateView.as_view()),
    path('list', FeedBackListView.as_view()),
    path('detail/<slug:slug_full_name>', FeedBackDetailView.as_view(), name='full-name-url'),
    path('<slug:slug_full_name>', FeedbackUpdateView.as_view())
]