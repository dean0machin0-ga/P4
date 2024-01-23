from django import forms
from .models import CustomUser, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email', 'bio', 'location', 'astrological_sign']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'username', 'content']