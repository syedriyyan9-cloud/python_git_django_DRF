from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView
    )
# from django.http import HttpResponse
# Create your views here.

posts = [{
    'author': 'riyyan',
    'title': 'Blog post 1',
    'content': 'something new',
    'date_posted': 'august 27, 2003'
},{
        'author': 'hassan',
    'title': 'Blog post 2',
    'content': 'something newer',
    'date_posted': 'august 01, 2009'
},{
        'author': 'syed',
    'title': 'Blog post 3',
    'content': 'something',
    'date_posted': 'octuber 27, 2003'
}]

def home(request):
    context = {'posts':posts}
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = 'Post'
    template_name = 'blog/home.html'    # app/model_viewtype.html
    context_object_name = 'posts'
    # ordering = [-'date_posted']

class PostDetailView(DetailView):
    model = 'Post'

class PostDetailView(CreateView):
    model = 'Post'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'blog/about.html')

