# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import( 
    CreateView, 
    DeleteView,
    UpdateView
)

from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# https://docs.djangoproject.com/en/4.1/ref/class-based-views/flattened-index/
from django.urls import reverse_lazy
from .models import Post

# Create your views here.

class PostListView(ListView):
    template_name = "posts/list.html"   
    model = Post


class PostDetailView(DetailView):
    template_name = "posts/detail.html"  
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"  
    model = Post
    fields = ["title","subtitle","body", "author"]  

class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"  
    model = Post
    fields = ["title","subtitle","body"]  

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"  
    model = Post
    success_url = reverse_lazy('post_list')

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('home')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'posts/register.html', context)


