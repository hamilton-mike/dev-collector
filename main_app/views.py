from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dev, Language, Photo
from .forms import InterviewForm
import os
import uuid
import boto3
import botocore.exceptions


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def devs_index(request):
    devs = Dev.objects.filter(user=request.user)
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

class DevCreate(LoginRequiredMixin, CreateView):
    model = Dev
    fields = ['name', 'location', 'age', 'bio', 'remote']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DevUpdate(LoginRequiredMixin, UpdateView):
    model = Dev
    fields = ['location', 'bio', 'remote']

class DevDelete(LoginRequiredMixin, DeleteView):
    model = Dev
    success_url = '/devs/'

@login_required
def add_interview(request, dev_id):
    form = InterviewForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
        new_interview = form.save(commit=False)
        new_interview.dev_id = dev_id
        new_interview.save()

    return redirect('detail', dev_id=dev_id)

class LanguageList(LoginRequiredMixin, ListView):
    model = Language

class LanguageDetail(LoginRequiredMixin, DetailView):
    model = Language

class LanguageCreate(LoginRequiredMixin, CreateView):
    model = Language
    fields = ['name']

class LanguageUpdate(LoginRequiredMixin, UpdateView):
    model = Language
    fields = ['name']

class LanguageDelete(LoginRequiredMixin, DeleteView):
    model = Language
    success_url = '/languages'

@login_required
def assoc_language(request, dev_id, language_id):
    Dev.objects.get(id=dev_id).languages.add(language_id)
    return redirect('detail', dev_id=dev_id)

@login_required
def add_photo(request, dev_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}/{key}"
      print(url)
      Photo.objects.create(url=url, dev_id=dev_id)
    except botocore.exceptions.ClientError as error:
      print('An error occurred uploading file to S3')
      raise error
    except botocore.exceptions.ParamValidationError as error:
      raise ValueError('The parameters you provided are incorrect: {}'.format(error))
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', dev_id=dev_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      print(f'User: {user}')
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid signup - Try Again'

  form = UserCreationForm()
  context = { 'form': form, 'error_message': error_message }
  return render(request, 'registration/signup.html', context)
