# Main_app/urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('about/', views.about, name='about'),
    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/<int:profile_id>/', views.profile_details, name='details'),
    path('profiles/create', views.ProfileCreate.as_view(), name='profile_create'),
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/create', views.CommentCreate.as_view(), name='comments_create'),
    path('search_results/', views.search_results, name='search_results'),
]