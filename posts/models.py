from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=70)
    short_description = models.CharField(max_length=150)
    content = models.TextField()
    image = models.URLField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    publish_Date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(
        'category.Category',
        help_text='Categorize this item.'
    )

    def __str__(self):
        return self.titulo