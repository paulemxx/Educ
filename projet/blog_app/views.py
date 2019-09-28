from django.shortcuts import render
from .models import *

# Create your views here.
def blog(request):
    cat_list = Categorie.objects.filter(statut=True)
    articles = Artcle.objects.filter(statut=True)
    data = {
        cat_list = cat_list,
        articles = articles,
    }
    return render(request, 'pages/blog.html', data)

def categorie(request, id_cat):
    return render(request, 'pages/blogcategorie.html')