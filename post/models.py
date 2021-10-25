from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    '''
        Model that handle user post
    '''
    title = models.CharField(
        max_length=256, verbose_name='Title of Post',  null=True, )
    post_content = models.CharField(
        max_length=1000, verbose_name='Post Content',   null=True,)
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owner',  null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created', )  # order by date of creation
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'New Post by {self.posted_by}'


class PostLike(models.Model):
    '''
        Model that handles likes
    '''
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_like')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_like_post')
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
