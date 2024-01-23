# Models
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# User Model
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
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


# Custom Profile Model
# class Profile(AbstractUser):
#     profile_img = models.ImageField(upload_to='profile_imgs/', blank=True)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=50, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     astrological_sign = models.CharField(max_length=50, blank=True)

#     def __str__(self):
#         return f'{self.username} ({self.id})'

#     def get_absolute_url(self):
#         return reverse('details')
    
# Tattoo Image Model
# class TattooImg(models.Model):
#     img = models.ImageField(upload_to="tattoo_imgs", blank=False)
#     like_dislike = models.BooleanField(default=False)
#     comments = models.ManyToManyField(Comment, related_name='tattoo_comments')
#     profile = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
#     # upload_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.img.name} (Likes: {self.like_dislike})'

#     def toggle_like_dislike(self):
#         self.like_dislike = not self.like_dislike
#         self.save()

#     def add_comment(self, comment_content, username):
#         comment_profile = get_user_model().objects.get(username=username).profile
#         comment = Comment.objects.create(title='', content=comment_content, username=username, profile=comment_profile)
#         self.comments.add(comment)
#         self.save()