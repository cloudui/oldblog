from django.shortcuts import render

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

from watson import search as watson



class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 5
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'



class SearchResultsListView(ListView):
    model = Post
    context_object_name = 'post_results'
    template_name = 'post_results.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('ques')
        return context 

    def get_queryset(self):
        query = self.request.GET.get('ques')
        search_results = watson.filter(Post, query)
              
        return search_results
    