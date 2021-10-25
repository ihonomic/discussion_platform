from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from post.serializers import PostLikeSerializer, PostSerializer
from .models import Post, PostLike
from rest_framework import permissions
from django.db.models import Q
from .permissions import IsOwnerOrReadOnly


class PostView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def post(self, request, *args, **kwargs):
        post = Post.objects.create(
            title=request.data['title'],
            post_content=request.data['post_content'],
            posted_by_id=request.user.id
        )
        post = self.serializer_class(post).data

        return Response(post, status='201')


class PostDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class TooglePostLikeView(ListCreateAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer

    def post(self, request, pk, *args, **kwargs):
        check_if_liked = PostLike.objects.filter(
            Q(post_id=pk) &
            Q(posted_by_id=request.user.id))
        if check_if_liked:
            check_if_liked.delete()
            return Response({'success': 'You unliked a post'}, status='200')
        else:
            PostLike.objects.create(
                post_id=pk,
                posted_by_id=request.user.id
            )
            return Response({'success': 'You like a post'}, status='200')
