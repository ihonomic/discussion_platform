from rest_framework import serializers
from .models import Post, PostLike
from users.serializers import UserSerializer


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id', 'post', 'user']


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post_like = serializers.SerializerMethodField('get_post_likers')
    total_like = serializers.SerializerMethodField('get_total_like')
    date_created = serializers.SerializerMethodField('get_date_created')

    class Meta:
        model = Post
        exclude = ['date_edited']

    def get_post_likers(self, obj):
        return PostLikeSerializer(PostLike.objects.filter(post_id=obj.id), many=True).data

    def get_total_like(self, obj):
        return PostLike.objects.filter(post_id=obj.id).count()

    def get_date_created(self, obj):
        return obj.date_created.date().isoformat()

        return post
