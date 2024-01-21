# Models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.conf import settings

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

# Comment Model
class Comment(models.Model):
    title = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50)
    content = models.TextField(max_length=750, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({self.username})'

# Tattoo Image Model
class TattooImg(models.Model):
    img = models.ImageField(upload_to="imgs", blank=False)
    like_dislike = models.BooleanField(default=False)
    comments = models.ManyToManyField(Comment, related_name='tattoo_comments')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.img.name} (Likes: {self.like_dislike})'

    def toggle_like_dislike(self):
        self.like_dislike = not self.like_dislike
        self.save()

    def add_comment(self, comment_content, username):
        comment = Comment.objects.create(title='', content=comment_content, username=username)
        self.comments.add(comment)
        self.save()





# Code In Limbo

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_or_update_profile(sender, instance, created, **kwargs):
#     if created:
#         if not hasattr(instance, 'profile'):
#             Profile.objects.create(user=instance)
#     else:
#         instance.profile.save()

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_user_profile(sender, instance, **kwargs):