from django.shortcuts import render

class Dev:
    def __init__(self, name, location, age, bio, remote):
        self.name = name
        self.location = location
        self.age = age
        self.bio = bio
        self.remote = remote

devs = [
    Dev('Ryan', 'Las Vegas, Nv', 21, 'Experimenting with HTML, CSS, and JavaScript; dabbling with Python and Ruby', True),
    Dev('Jamie', 'Sacramento, Ca', 41, 'A freelance British web designer and developer', False),
    Dev('Curtis', 'Phoenix, Az', 30, 'Im supposed to come up with a bio?!', True)
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def devs_index(request):
    return render(request, 'devs/index.html', { 'devs': devs })
