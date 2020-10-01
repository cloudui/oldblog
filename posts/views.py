from django.shortcuts import render

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

from django.http import Http404
from watson import search as watson



class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 5
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(visible=True)

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

    def dispatch(self, request, *args, **kwargs):
        
        
        if not self.get_object().visible:
            print(self.get_object().visible)
            raise Http404
        
        return super().dispatch(request, *args, **kwargs)
                

    
class AboutPageView(TemplateView):
    template_name = 'about.html'


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
        search_results = watson.filter(Post, query).filter(visible=True)
              
        return search_results
    
class ZoomLinks(TemplateView):
    template_name = 'zoom.html'