from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('home/', views.home, name='home'),
    path('about_us/', views.sobre_nosotros, name='sobre_nosotros'),
]
