from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostListSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'short_description', 'categories']


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'short_description', 'content', 'image', 'video', 'publish_Date', 'creation_date', 'modification_date', 'owner', 'categories']
        read_only_fields = ['id', 'creation_date', 'modification_date']