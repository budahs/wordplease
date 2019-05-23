from django.contrib import admin
from django.urls import path

from posts.views import LatestPostViews, PostView, CreatePostView, UserBlogView
from users.views import LogoutView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Users
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # Posts
    path('new-post/', CreatePostView.as_view(), name='create_post'),
    path('blogs/<str:username>/', UserBlogView.as_view(), name='user_blog'),
    path('blogs/<str:username>/<int:pk>/', PostView.as_view(), name='post'),
    path('', LatestPostViews.as_view(), name='home')
]
