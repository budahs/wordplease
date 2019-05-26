import datetime

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from posts.models import Post
from posts.serializers import PostListSerializer, PostSerializer


class PostsAPI(ListCreateAPIView):

    permission_classes = [AllowAny]

    def get_queryset(self):
        blog_user = self.kwargs.get('username')
        queryset = Post.objects.filter(publish_Date__lte=datetime.datetime.now(), owner__username=blog_user).order_by('-modification_date').select_related('owner')

        if (self.request.user.is_authenticated and blog_user == self.request.user.username) or self.request.user.is_superuser:
            queryset = Post.objects.filter(owner__username=blog_user).order_by(
            '-modification_date').select_related('owner')

        return queryset

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == 'GET' else PostSerializer
        #return super().get_serializer_class()

class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer