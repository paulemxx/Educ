from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def contact(request):
    if request.POST is not None:
        ca = Contact_us(
            nom = request.POST.get('name')
            email = request.POST.get('email')
            sujet = request.POST.get('subject')
            message = request.POST.get('message')
        )
        ca.save()
        ne = Newsletter(
            email = request.POST.get('email')
        )
        ne.save()
        return redirect('home')
    return render(request, 'pages/contact.html')

def Newsletter(request):
    if request.POST is not None:
        ne = Newsletter(
            email = request.POST.get('email')
        )
        ne.save()
        return redirect('home')
    return render(request, 'pages/index.html')
