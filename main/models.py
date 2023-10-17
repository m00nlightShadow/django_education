from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Topic(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    user = models.ManyToManyField(User, through='Preference', related_name='topics')

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    topic = models.ManyToManyField(Topic, related_name='articles')

    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.message


class Preference(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notify = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.topic}'
