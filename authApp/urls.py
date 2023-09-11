from django.urls import path, include
from authApp import views
urlpatterns = [
    path('', views.HomeView)
]
