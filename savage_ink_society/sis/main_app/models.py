from django.db import models
from django.contrib.auth.models import User

# Profile Model
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_img = models.ImageField(upload_to='profile_imgs/', blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)