# main_app/views 
import requests
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Profile, TattooImg, TattooShop, Comment, BackgroundImage, Comment
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