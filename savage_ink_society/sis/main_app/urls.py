# main_app/urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    # path('profile/create', views.ProfileCreate.as_view(), name='profile_create'),
]