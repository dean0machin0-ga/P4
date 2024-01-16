from django.db import models
from django.contrib.auth.models import User

# Profile Model
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    userbio = models.TextField(max_length=500, blank=True)