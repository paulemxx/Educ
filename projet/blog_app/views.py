from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'pages/blog.html')

def categorie(request):
    return render(request, 'pages/blogcategorie.html')