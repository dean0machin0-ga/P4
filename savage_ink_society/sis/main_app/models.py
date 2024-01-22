# Models
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Custom Profile Model
class Profile(AbstractUser):
    profile_img = models.ImageField(upload_to='profile_imgs/', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    astrological_sign = models.CharField(max_length=50, blank=True)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['bio', 'location', 'birth_date', 'astrological_sign']
    
    def __str__(self):
        return f'{self.username} ({self.id})'

    def get_absolute_url(self):
        return reverse('details')

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

# Tattoo Image Model
class TattooImg(models.Model):
    img = models.ImageField(upload_to="imgs", blank=False)
    like_dislike = models.BooleanField(default=False)
    comments = models.ManyToManyField(Comment, related_name='tattoo_comments')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.img.name} (Likes: {self.like_dislike})'

    def toggle_like_dislike(self):
        self.like_dislike = not self.like_dislike
        self.save()

    def add_comment(self, comment_content, username):
        comment = Comment.objects.create(title='', content=comment_content, username=username)
        self.comments.add(comment)
        self.save()

class BackgroundImage(models.Model):
    img_url = models.URLField()
    caption = models.CharField(max_length=225)