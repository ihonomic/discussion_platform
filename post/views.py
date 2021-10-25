from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from post.serializers import PostSerializer
from .models import Post, PostLike
from rest_framework import permissions
from django.http.response import Http404


class IsOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False


class PostView(APIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner, )

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        queryset = Post.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status='200')

    def post(self, request, format=None):
        Post.objects.create(
            title=request.data['title'],
            post_content=request.data['post_content'],
            user_id=request.user.id
        )

        return Response({'success': 'New Post added'}, status='201')

    def put(self, request, format=None):
        #   Update other details
        serializer = self.serializer_class(
            user_obj, data=data)
        if serializer.is_valid():
            serializer.save()


class LikeAPostView(APIView):
    ...
