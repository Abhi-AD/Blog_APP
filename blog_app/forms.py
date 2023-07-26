from django import forms
from blog_app.models import Post

class PostForm(forms.ModelForm):
     class Meta:
          model = Post
          fields = ("title", "content")