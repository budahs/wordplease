import datetime

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from posts.forms import PostsForm
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

def create_post(request):
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post created successfully with ID {0}'.format(new_post.pk))
            form = PostsForm()
    else:
        form = PostsForm()

    context = {'form': form}
    return render(request, 'posts/new.html', context)