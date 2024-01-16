# main_app/urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('about/', views.about, name='about'),
]