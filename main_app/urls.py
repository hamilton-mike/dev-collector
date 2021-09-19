from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('devs/', views.devs_index, name='index'),
    path('devs/<int:dev_id>', views.devs_detail, name='detail'),
    path('devs/create', views.DevCreate.as_view(), name='devs_create'),
    path('devs/<int:pk>/update', views.DevUpdate.as_view(), name='devs_update'),
    path('devs/<int:pk>/delete', views.DevDelete.as_view(), name='devs_delete'),
]
