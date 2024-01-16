# main_app/views 
from django.shortcuts import render

# Create your views here.

# Splash View
def splash(request):
    return render(request, 'splash.html')

# About View
def about(request):
    return render(request, 'about.html')

# Profile View
def profile(request):
    return render(request, 'profile.html')

# Profile Create View
# class ProfileCreate(CreateView):
#     model = Profile
#     fields = __all__