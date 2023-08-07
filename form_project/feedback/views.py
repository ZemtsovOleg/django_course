from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .forms import FeedbackForm
from .models import Feedback

# Create your views here.


class FeedbackCreateView(CreateView):
    model = Feedback
    # fields = '__all__'
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    # success_url = 'done'


class FeedbackUpdateView(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = 'done'
    slug_url_kwarg = 'slug_full_name'


class DoneTemplateView(TemplateView):
    template_name = 'feedback/done.html'


class FeedBackListView(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    context_object_name = 'feedbacks_data'  # 'object_list'
    queryset = Feedback.objects.filter(tattoo=True)


class FeedBackDetailView(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback
    slug_url_kwarg = 'slug_full_name'


# def index(request):
#     if request.method == 'POST':
#         print(request.POST)
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             print('form.cleaned_data:', form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('done/')
#     else:
#         form = FeedbackForm()
#     return render(request, 'feedback/feedback.html', context={'form': form})

# class FeedbackView(View):
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, 'feedback/feedback.html', context={'form': form})

#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('done')
#         return render(request, 'feedback/feedback.html', context={'form': form})

# class ListFeedBackTemplateView(TemplateView):
#     template_name = 'feedback/list_feedback.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         feedbacks_data = Feedback.objects.all()
#         context['feedbacks_data'] = feedbacks_data
#         return context

# class DetailFeedBack(TemplateView):
#     template_name = 'feedback/detail_feedback.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         feedback_data = Feedback.objects.get(id=kwargs['id_feedback'])
#         context['id'] = feedback_data
#         return context

# class FeedbackView(FormView):
#     form_class = FeedbackForm
#     template_name = 'feedback/feedback.html'
#     success_url = 'done'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# class FeedbackUpdateView(View):
#     def get(self, request, id_feedback):
#         feedback_data = get_object_or_404(Feedback, id=id_feedback)
#         form = FeedbackForm(instance=feedback_data)
#         return render(request, 'feedback/feedback.html', context={'form': form})

#     def post(self, request, id_feedback):
#         feedback_data = Feedback.objects.get(id=id_feedback)
#         form = FeedbackForm(request.POST, instance=feedback_data)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('done')
#         return render(request, 'feedback/feedback.html', context={'form': form})
