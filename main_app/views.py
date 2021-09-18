from django.shortcuts import render
from .models import Dev

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def devs_index(request):
    devs = Dev.objects.all()
    return render(request, 'devs/index.html', { 'devs': devs })
