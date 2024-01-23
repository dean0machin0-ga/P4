# Models
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# User Model
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=250, blank=True)
    location = models.CharField(max_length=255, blank=True)
    astrological_sign = models.CharField(max_length=50, blank=True)

# Comment Model
class Comment(models.Model):
    title = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50)
    content = models.TextField(max_length=750, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({self.username})'
    
    def get_absolute_url(self):
        return reverse('comment_detail', args=[str(self.id)])

# Photo Model
class Photo(models.Model):
    url = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"My dream tattoo profile_id: {self.user_id} @{self.url}"

# Background Img Model
class BackgroundImage(models.Model):
    img_url = models.URLField()
    caption = models.CharField(max_length=225)

# # API Model
class TattooShop(models.Model):
    name = models.CharField(max_length=255)
    rating = models.FloatField()
    review_count = models.IntegerField()
    price_range = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    business_page_link = models.URLField()
    photo = models.URLField()