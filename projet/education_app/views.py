from django.shortcuts import render
from blog_app.models import *

# Create your views here.
def index(request):
    cat_list = Categorie.objects.filter(statut=True)
    data = {
        'cat_list': cat_list,
    }
    return render(request, 'pages/index.html', data)

def theme(request):
    return render(request, 'pages/coursdetail.html')

def cours(request):
    return render(request, 'pages/cours.html')

def about(request):
    return render(request, 'pages/about.html')

def category(request):
    return render(request, 'pages/category.html')

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')