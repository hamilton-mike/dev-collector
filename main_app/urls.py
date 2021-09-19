from django.urls import path, include
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
    path('languages/', views.LanguageList.as_view(), name='languages_list'),
    path('languages/create', views.LanguageCreate.as_view(), name='languages_create'),
    path('languages/<int:pk>', views.LanguageDetail.as_view(), name='languages_detail'),
    path('languages/<int:pk>/update', views.LanguageUpdate.as_view(), name='languages_update'),
    path('languages/<int:pk>/delete', views.LanguageDelete.as_view(), name='languages_delete'),
    path('devs/<int:dev_id>/assoc_language/<int:language_id>/', views.assoc_language, name='assoc_language'),
    path('devs/<int:dev_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/', include('django.contrib.auth.urls'))
]
