from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post, Image

from django.http import Http404
from watson import search as watson
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy, reverse_lazy

from django.utils.text import slugify

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


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
        obj = self.get_object()
        
        if not obj.visible:
            if self.request.user.is_authenticated:
                if self.request.user.is_staff:
                    return redirect('preview', obj.slug)
            else:
                raise Http404
        
        return super().dispatch(request, *args, **kwargs)

class PostPreviewView(DetailView):
    model = Post
    template_name = 'admin/detail.html'

    def dispatch(self, request, *args, **kwargs):
        
        
        if self.request.user.is_authenticated:
            if not self.request.user.is_staff:
                raise PermissionDenied
        else:
            raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)
                

    
class AboutPageView(TemplateView):
    template_name = 'about.html'


class SearchResultsListView(ListView):
    model = Post
    context_object_name = 'post_results'
    template_name = 'post_results.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context 

    def get_queryset(self):
        query = self.request.GET.get('q')
        search_results = watson.filter(Post, query).filter(visible=True)
              
        return search_results
    
class ZoomLinks(TemplateView):
    template_name = 'zoom.html'


class ImageView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'images.html'

class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    context_object_name = 'post'
    template_name = 'admin/create.html'
    fields = ('title', 'body', 'body_short',)
    login_url = 'login'
    success_message = 'Post Created'
    
    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)

        return super(PostCreateView, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        
        
        if self.request.user.is_authenticated:
            if not self.request.user.is_staff:
                raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)

class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'admin/update.html'
    fields = '__all__'
    login_url = 'login'
    context_object_name = 'post'
    success_message = 'Post Edited'

    def dispatch(self, request, *args, **kwargs):
        
        
        if self.request.user.is_authenticated:
            if not self.request.user.is_staff:
                raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'admin/delete.html'
    login_url = 'login'
    context_object_name = 'post'
    success_url = reverse_lazy('admin')

    def dispatch(self, request, *args, **kwargs):
        
        
        if self.request.user.is_authenticated:
            if not self.request.user.is_staff:
                raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)


class PostAdminView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'admin/admin.html'
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        
        
        if self.request.user.is_authenticated:
            if not self.request.user.is_staff:
                raise PermissionDenied        
        return super().dispatch(request, *args, **kwargs)

