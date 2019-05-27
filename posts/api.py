import datetime

from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated

from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostListSerializer, PostSerializer


class PostsAPI(ListAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'short_description', 'categories__title']
    order_fields = ['id', 'creation_date', 'modification_date', 'title']

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
    permission_classes = [PostPermission]
    serializer_class = PostSerializer

class CreatePostAPI(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
