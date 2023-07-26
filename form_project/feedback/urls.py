from django.urls import path

from .views import FeedBackListView, DoneTemplateView, FeedbackUpdateView, FeedbackCreateView, FeedBackDetailView

urlpatterns = [
    path('', FeedbackCreateView.as_view()),
    path('done', DoneTemplateView.as_view()),
    path('list', FeedBackListView.as_view()),
    path('detail/<int:pk>', FeedBackDetailView.as_view()),
    path('<int:pk>', FeedbackUpdateView.as_view())
]