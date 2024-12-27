from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy

from .forms import UpdateUserForm, UserCreationForm
from django.contrib.auth.models import User
from appPost.models import Post 
from django.views.generic import DetailView, CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

# Create your views here.

class LoginUserView (LoginView) : 
    template = './templates/appuser/login_user.html '

class RegisterUserView(CreateView): 
    model = User 
    form_class= UserCreationForm
    template = './templates/appuser/user_form.html'
    success_url = reverse_lazy('appPost:menu')
    
class UpdateUserView(LoginRequiredMixin, UpdateView): 
    model = User 
    form_class= UpdateUserForm
    template = './templates/appuser/edit_user.html' 
   

class DeleteUserView(LoginRequiredMixin, DeleteView): 
    model = User 
    template = './templates/appuser/delete_user.html'
    success_url = reverse_lazy('appuser:login')

class DetailUserView(LoginRequiredMixin, DetailView): 
    model = User
    template_name = './templates/appuser/detail_user.html'
    context_object_name = 'user'


def get_user(request): 
    user = User.objects.all()
    return render(request, './appuser/lista.html', {'users' : user})


def get_all_user_post (request, pk): 
    posts = Post.objects.filter(user=pk).values()
    return render(request, './templates/appuser/ver_posts.html', {'posts' : posts})
