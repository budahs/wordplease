from django.contrib import admin
from django.urls import path

from posts.views import latest_posts, post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/<int:pk>/', post, name='post'),
    path('', latest_posts, name='home')
]
