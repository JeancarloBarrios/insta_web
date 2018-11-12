from django.db import models
from django.conf import settings

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    files = models.ManyToManyField(
        'files.File',
        through='PostFile'
    )
    tags = models.ManyToManyField(
        'Tag',
        through='PostTag'
    )


class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)
    posts = models.ManyToManyField(
        'Post',
        through='PostTag',
    )


class PostTag(models.Model):
    tag = models.ForeignKey(
        'Tag',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE
    )


class PostFile(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE
    )
    file = models.ForeignKey(
        'files.File',
        on_delete=models.CASCADE
    )
