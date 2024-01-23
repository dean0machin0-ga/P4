from django import forms
from .models import CustomUser, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name','last_name', 'email', 'bio', 'location', 'astrological_sign']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Save'))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'username', 'content']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Put In Ink', css_class='btn btn-dark mt-3; background-color: black', attrs={'style': 'background-color: black; color: white; border: 1px solid white;'}))