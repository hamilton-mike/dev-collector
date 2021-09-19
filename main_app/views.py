from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dev

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def devs_index(request):
    devs = Dev.objects.all()
    return render(request, 'devs/index.html', { 'devs': devs })

def devs_detail(request, dev_id):
    dev = Dev.objects.get(id=dev_id)
    return render(request, 'devs/detail.html', { 'dev': dev })

class DevCreate(CreateView):
    model = Dev
    fields = '__all__'

class DevUpdate(UpdateView):
    model = Dev
    fields = ['location', 'bio', 'remote']

class DevDelete(DeleteView):
    model = Dev
    success_url = '/devs/'
