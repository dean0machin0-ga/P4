# main_app/views 
from django.shortcuts import render

# Create your views here.

# Splash Page
def splash(request):
    return render(request, 'splash.html')