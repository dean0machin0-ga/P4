# main_app/views 
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Profile

# Create your views here.

# Splash View
def splash(request):
    return render(request, 'splash.html')

# About View
def about(request):
    return render(request, 'about.html')

# Profile list 
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/list.html', {
        'profiles': profiles
    })
    
# Profile Detail
def profile_details(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profiles/details.html', {
        'profile': profile
    })

# Profile Create View
# class ProfileCreate(CreateView):
#     model = Profile
#     fields = __all__