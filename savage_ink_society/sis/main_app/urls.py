# Main_app/urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('about/', views.about, name='about'),
    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/<int:profile_id>/', views.profile_details, name='details'),
    path('profiles/create', views.ProfileCreate.as_view(), name='profile_create'),
    path('profiles/<int:profile_id>/add_photo/', views.add_photo, name='add_photo'),
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/create', views.CommentCreate.as_view(), name='comments_create'),
    path('comments/<int:pk>/update/', views.CommentUpdate.as_view(), name='comments_update'),
    path('comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comments_delete'),
    path('comments/<int:comment_id>/', views.comment_detail, name='comment_detail'),
    path('search_results/', views.search_results, name='search_results'),
    path('tattoo_imgs/', views.tattoo_list, name='tattoo_list'),
]
