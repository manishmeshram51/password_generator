from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('generated_password',views.password_generator, name = 'generate_password'),
]
