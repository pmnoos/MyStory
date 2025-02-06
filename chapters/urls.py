from django.contrib.auth import views as auth_views
from .views import custom_login
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('chapter/new/', views.new_chapter, name='new_chapter'),
    path('chapters', views.chapter_list, name='chapter_list'),
    path('<slug:slug>/', views.chapter_detail, name='chapter_detail'),
    path('chapter/<slug:slug>/edit/', views.edit_chapter, name='edit_chapter'),
]
