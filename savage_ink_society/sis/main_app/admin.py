from django.contrib import admin
from .models import CustomUser, Comment, Photo

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Comment)
admin.site.register(Photo)