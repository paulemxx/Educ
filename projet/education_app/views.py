from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

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