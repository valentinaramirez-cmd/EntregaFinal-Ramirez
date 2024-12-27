from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView
from .forms import PostForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView (LoginRequiredMixin, TemplateView): 
    template = './appPost/menu.html'

class CreatePostView (LoginRequiredMixin, CreateView): 
    model = Post
    fields = ['texto', 'titulo']
    template = './appPost/post_form.html'
    success_url = reverse_lazy('appPost:menu')

def create_post (request): 
    if request.method == 'POST' : 
        form = PostForm(request.POST) 

        if form.is_valid() : 
            form.save()
            return redirect('appPost:menu')
            
    else: 
        form = PostForm()

    return render(request, './appPost/create_post.html', {'form' : form})

def get_posts(request): 
    posts = Post.objects.all()
    return render(request, './appPost/listar_posts.html', {'posts' : posts})

    