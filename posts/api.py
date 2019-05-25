from rest_framework.generics import ListCreateAPIView

from posts.models import Post
from posts.serializers import PostListSerializer, PostSerializer


class PostsAPI(ListCreateAPIView):

    queryset = Post.objects.all()

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == 'GET' else PostSerializer
        #return super().get_serializer_class()