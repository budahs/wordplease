from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.views import View

from posts.models import Post
from users.forms import LoginForm


class LoginView(View):

    def render_template_with_form(self, request, form):
        context = {'form': form}
        return render(request, 'users/login.html', context)

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = LoginForm()
        return self.render_template_with_form(request, form)

    def post(self, request):

        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Usuario/contraseña incorrectos')
            else:
                django_login(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)

        return self.render_template_with_form(request, form)


class LogoutView(View):

    def get(self, request):
        django_logout(request)
        return redirect('login')