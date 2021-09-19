from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dev, Language
from .forms import InterviewForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def devs_index(request):
    devs = Dev.objects.all()
    return render(request, 'devs/index.html', { 'devs': devs })

def devs_detail(request, dev_id):
    try:
        dev = Dev.objects.get(id=dev_id)
        languages_dev_doesnt_have = Language.objects.exclude(id__in = dev.languages.all().values_list('id'))
        interview_form = InterviewForm()
        return render(request, 'devs/detail.html', {
            'dev': dev ,
            'interview_form': interview_form,
            'languages': languages_dev_doesnt_have
        })
    except(Dev.DoesNotExist):
        return redirect('/devs')

class DevCreate(CreateView):
    model = Dev
    fields = ['name', 'location', 'age', 'bio', 'remote']

class DevUpdate(UpdateView):
    model = Dev
    fields = ['location', 'bio', 'remote']

class DevDelete(DeleteView):
    model = Dev
    success_url = '/devs/'

def add_interview(request, dev_id):
    form = InterviewForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
        new_interview = form.save(commit=False)
        new_interview.dev_id = dev_id
        new_interview.save()

    return redirect('detail', dev_id=dev_id)

class LanguageList(ListView):
    model = Language

class LanguageDetail(DetailView):
    model = Language

class LanguageCreate(CreateView):
    model = Language
    fields = ['name']

class LanguageUpdate(UpdateView):
    model = Language
    fields = ['name']

class LanguageDelete(DeleteView):
    model = Language
    success_url = '/languages'

def assoc_language(request, dev_id, language_id):
    Dev.objects.get(id=dev_id).languages.add(language_id)
    return redirect('detail', dev_id=dev_id)
