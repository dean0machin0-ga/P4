# Models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.conf import settings

# Custom Profile Model
class Profile(AbstractUser):
    profile_img = models.ImageField(upload_to='profile_imgs/', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    astrological_sign = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f'{self.username} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail')

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_or_update_profile(sender, instance, created, **kwargs):
#     if created:
#         if not hasattr(instance, 'profile'):
#             Profile.objects.create(user=instance)
#     else:
#         instance.profile.save()

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_user_profile(sender, instance, **kwargs):