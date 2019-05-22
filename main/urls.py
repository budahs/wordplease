from django.contrib import admin
from django.urls import path

from posts.views import latest_posts, post
from users.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    # Users
    path('login', login, name='login'),
    # Posts
    path('post/<int:pk>/', post, name='post'),
    path('', latest_posts, name='home')
]
