from django.contrib import admin
from django.urls import path

from posts.views import latest_posts, post, create_post
from users.views import login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    # Users
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    # Posts
    path('post/new/', create_post, name='create_post'),
    path('post/<int:pk>/', post, name='post'),
    path('', latest_posts, name='home')
]
