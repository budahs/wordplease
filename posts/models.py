import datetime

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=70)
    short_description = models.CharField(max_length=150)
    content = models.TextField()
    image = models.URLField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    publish_Date = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now())
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    categories = models.ManyToManyField(
        'category.Category',
        help_text='Set prefered categories.'
    )

    def __str__(self):
        return self.title