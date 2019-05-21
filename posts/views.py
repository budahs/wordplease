from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    name = request.GET.get('name', 'world')
    order = request.GET.get('order', 'planet')
    response = 'Hello {0}, I am a {1}'.format(name, order)
    return HttpResponse(response)
