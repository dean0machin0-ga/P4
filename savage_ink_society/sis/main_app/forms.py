from django import forms
from .models import Profile, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_img', 'bio', 'location', 'birth_date', 'astrological_sign']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'username', 'content']