from django.shortcuts import render

class Dev:
    def __init__(self, name, location, age, remote):
        self.name = name
        self.location = location
        self.age = age
        self.remote = remote

devs = [
    Dev('Ryan', 'Las Vegas, Nv', 21, True),
    Dev('Jamie', 'Sacramento, Ca', 41, False),
    Dev('Curtis', 'Phoenix, Az', 30, True)
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def devs_index(request):
    return render(request, 'devs/index.html', { 'devs': devs })
