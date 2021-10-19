
from django.contrib import admin
from django.urls import path

from popup import views

urlpatterns = [
    path('', views.popup, name='popup'),
]
