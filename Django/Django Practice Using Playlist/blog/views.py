from django.shortcuts import render
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

def about(request):
    return render(request, 'blog/about.html')

