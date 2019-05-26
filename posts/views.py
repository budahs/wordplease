import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from posts.forms import PostsForm
from posts.models import Post


class LatestPostViews(View):

    def get(self, request):
        posts = Post.objects.all().filter(publish_Date__lte=datetime.datetime.now()).order_by('-modification_date').select_related('owner')
        context = {'posts': posts[:6]}
        html = render(request, 'posts/latest.html', context)

        return HttpResponse(html)

class UserBlogView(View):
    def get(self, request, username):
        posts = Post.objects.all().filter(owner__username=username).select_related('owner')
        context = {'posts': posts}
        html = render(request, 'posts/latest.html', context)
        return HttpResponse(html)

class PostView(View):

    def get(self, request, username, pk):
        post = get_object_or_404(Post.objects.select_related('owner'), pk=pk)
        context = {'post': post}
        html = render(request, 'posts/post.html', context)

        return HttpResponse(html)

# Ojo el decorador la url a la que redirigimos está en settings definida como LOGIN_URL
# @login_required # desaparece porque no es apropiado para clases. Ahora vamos a usar mixin de herencia multiple


class CreatePostView(LoginRequiredMixin, View):
    def return_post_with_form(self, request, form):
        context = {'form': form}
        return render(request, 'posts/new.html', context)

    def get(self, request):
        form = PostsForm()
        return self.return_post_with_form(request, form)

    def post(self, request):
        post = Post()
        post.owner = request.user
        form = PostsForm(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post created successfully with ID {0}'.format(new_post.pk))
            form = PostsForm()

        return self.return_post_with_form(request, form)

