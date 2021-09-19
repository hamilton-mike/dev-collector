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
    path('devs/<int:dev_id>/add_interview', views.add_interview, name='add_interview'),
    path('laguages/', views.LanguageList.as_view(), name='languages_list'),
    path('laguages/create', views.LanguageCreate.as_view(), name='languages_create'),
    path('laguages/<int:pk>', views.LanguageDetail.as_view(), name='languages_detail'),
    path('laguages/<int:pk>/update', views.LanguageUpdate.as_view(), name='languages_update'),
    path('laguages/<int:pk>/delete', views.LanguageDelete.as_view(), name='languages_delete')
]
