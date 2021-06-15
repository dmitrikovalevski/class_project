from django.forms import ModelForm
from .models import Post, Img


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class ImgForm(ModelForm):
    class Meta:
        model = Img
        fields = ['image']