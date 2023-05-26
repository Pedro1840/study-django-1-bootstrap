from django.contrib import admin
from django.urls import path
from . import views

APP_NAME = 'api_food'

urlpatterns = [
    path('', views.home, name="home")
]
