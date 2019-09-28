from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def theme(request):
    return render(request, 'pages/coursdetail.html')

def cours(request):
    return render(request, 'pages/cours.html')
