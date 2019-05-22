from django.forms import ModelForm

from posts.models import Post


class PostsForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'short_description', 'content', 'image', 'video', 'publish_Date', 'categories']