"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site
from . import views

app_name='education_app'
urlpatterns = [
    path('', views.index, name='home'),
    path('theme/', views.theme, name='detail'),
    path('cours/', views.cours, name='cours'),
    path('about/', views.about, name='about'),
    path('categorie/', views.category, name='category'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    
]
