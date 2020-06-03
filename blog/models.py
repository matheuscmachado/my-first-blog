from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    Class Post: Make a post on the site
    --------
    Attributes:
    title (string): Title of the post
    text (string): Text of the post
    author (string): Author of the post
    created_date (date): date of the creation of the post
    published_date (date): date of publishing of the post

    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
