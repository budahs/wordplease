import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from posts.models import Post


def latest_posts(request):

    posts = Post.objects.all().filter(publish_Date__lte=datetime.datetime.now()).order_by('-modification_date')
    context = {'posts': posts[:4]}
    html = render(request, 'posts/latest.html', context)

    return HttpResponse(html)


def post(request, pk):

    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    html = render(request, 'posts/post.html', context)

    return HttpResponse(html)