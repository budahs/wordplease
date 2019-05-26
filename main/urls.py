from django.contrib import admin
from django.urls import path

from posts.api import PostsAPI, PostDetailAPI, CreatePostAPI
from posts.views import LatestPostViews, PostView, CreatePostView, UserBlogView
from users.api import UserAPI, UserDetailAPI, ListBlogs
from users.views import LogoutView, LoginView, BlogListView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Users
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # Posts
    path('new-post/', CreatePostView.as_view(), name='create_post'),
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blogs/<str:username>/', UserBlogView.as_view(), name='user_blog'),
    path('blogs/<str:username>/<int:pk>/', PostView.as_view(), name='post'),
    path('', LatestPostViews.as_view(), name='home'),
    # API
    path('api/users/', UserAPI.as_view(), name='users_api'),
    path('api/users/<int:pk>/', UserDetailAPI.as_view(), name='user_detail_api'),
    path('api/posts/', CreatePostAPI.as_view(), name='create_post_api'),
    path('api/posts/<str:username>/', PostsAPI.as_view(), name='posts_api'),
    path('api/posts/<int:pk>', PostDetailAPI.as_view(), name='post_detail_api'),
    path('api/blogs/', ListBlogs.as_view(), name='blog_list_api')
]
