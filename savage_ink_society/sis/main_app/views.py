# main_app/views 
import os
import uuid
import boto3
import requests
from django.apps import AppConfig
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProfileForm, CommentForm
from .models import CustomUser, Photo, TattooShop, Comment, BackgroundImage, Comment
# from django.conf import settings

# Create your views here.

class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'

    def ready(self):
        import main_app.signals

# Splash View
def splash(request):
    background_images = BackgroundImage.objects.all()
    if background_images:
        background_image = random.choice(background_images)
    else:
        background_image = None

    return render(request, 'splash.html', {'background_image': background_image})

# About View
def about(request):
    return render(request, 'about.html')

# PROFILE VIEWS

# Profile Create
class ProfileCreate(CreateView):
    model = CustomUser
    form_class = ProfileForm
    template_name = 'profiles/profile_form.html' 
    success_url = reverse_lazy('profile_list')

# Profile list 
def profile_list(request):
    profiles = CustomUser.objects.all()
    return render(request, 'profiles/list.html', {
        'profiles': profiles
    })
    
# Profile Detail
def profile_details(request, profile_id):
    profile = CustomUser.objects.get(id=profile_id)
    # tattoo_imgs = TattooImg.objects.filter(comments__username=profile.username)
    comments = Comment.objects.filter(username=profile.username)
    
    return render(request, 'profiles/details.html', {
        'profile': profile,
        # 'tattoo_imgs': tattoo_imgs,
        'comments': comments,
    })

# Add Photo View
def add_photo(request, profile_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, profile_id=profile_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('details', profile_id=profile_id)

# COMMENT VIEWS

# Comment List
def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comments/list.html', {
        'comments': comments
    })

# Comment Detail
def comment_detail(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    return render(request, 'comments/comment_details.html', {
        'comment': comment,
    })

# Comment Create
class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/comment_form.html' 
    success_url = reverse_lazy('comment_list')

# Comment Update
class CommentUpdate(UpdateView):
    model = Comment
    fields = ['title', 'content']
    template_name = 'comments/comment_form.html' 
    
# Comment Delete
class CommentDelete(DeleteView):
    model = Comment
    template_name = 'comments/comment_confirm_delete.html'
    success_url = reverse_lazy('comment_list')

# TATTOO IMG VIEWS

# Tattoo Img List
def tattoo_list(request):
    tattoos = TattooImg.objects.all()
    return render(request, 'tattoo_imgs/list.html', {
        'tattoos' : tattoos,
    })

# Tattoo Details
# class TattooImgDetail(DetailView):
#     model = TattooImg
#     template_name = 'tattoo_img/tattoo_img_details.html'
#     context_object_name = 'tattoo_img'

#  Tattoo Toggle
# def toggle_like_dislike(request, tattoo_img_id):
#     tattoo_img = get_object_or_404(TattooImg, id=tattoo_img_id)
#     tattoo_img.like_dislike = not tattoo_img.like_dislike
#     tattoo_img.save()

#     return JsonResponse({'success': True})

# SEARCH VIEWS

# Artist Search View
def search_results(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')

        url = "https://yelp-reviews.p.rapidapi.com/business-search"

        headers = {
            "X-RapidAPI-Key": "71b12d4b25mshb3f90218c7116aap18f41ejsnd8bd73c57ee9",
            "X-RapidAPI-Host": "yelp-reviews.p.rapidapi.com"
        }
        params = {
            "query": search_query,
            "location": "Seattle, WA, USA",
            "start": "0",
            "yelp_domain": "yelp.com"
        }
        response = requests.get(url, headers=headers, params=params)

        print(response.json())
        api_data = response.json().get('businesses', [])

        for shop_data in api_data:
            TattooShop.objects.create(
                name=shop_data.get('name', ''),
                rating=shop_data.get('rating', 0.0),
                review_count=shop_data.get('review_count', 0),
                price_range=shop_data.get('price', ''),
                address=shop_data.get('location', {}).get('address1', ''),
                phone=shop_data.get('phone', ''),
                business_page_link=shop_data.get('url', ''),
                photo=shop_data.get('image_url', '')
            )

        tattoo_shops = TattooShop.objects.all()

        return render(request, 'search_results.html', {'tattoo_shops': tattoo_shops, 'search_query': search_query})
    else:
        return render(request, 'splash.html')