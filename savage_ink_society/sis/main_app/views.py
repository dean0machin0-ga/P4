# main_app/views 
import requests
from django.conf import settings
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Profile, TattooImg, Comment, BackgroundImage, Comment
from django.urls import reverse_lazy
from .forms import ProfileForm, CommentForm

# Create your views here.

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
    model = Profile
    form_class = ProfileForm
    # fields = ['profile_img', 'bio', 'location', 'birth_date', 'astrological_sign']
    template_name = 'profiles/profile_form.html' 
    success_url = reverse_lazy('profile_list')

# Profile list 
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/list.html', {
        'profiles': profiles
    })
    
# Profile Detail
def profile_details(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    tattoo_imgs = TattooImg.objects.filter(comments__username=profile.username)
    comments = Comment.objects.filter(username=profile.username)
    
    return render(request, 'profiles/details.html', {
        'profile': profile,
        'tattoo_imgs': tattoo_imgs,
        'comments': comments,
    })

# COMMENT VIEWS

# Comment List
def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comments/list.html', {
        'comments': comments
    })

# Comment Create
class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/comment_form.html' 
    success_url = reverse_lazy('comment_list')

# Artist Search Views
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

        results = response.json().get('businesses', [])

        return render(request, 'search_results.html', {'results': results, 'search_query': search_query})
    else:
        return render(request, 'splash.html')