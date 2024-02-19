from django import forms
from posts.models import PostModel


class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['image', 'title', 'description']