from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from post.models import User, Post, Comment
from post.serializers import UserSerializer, PostSerializer, CommentSerializer

from .permissions import PermissionPolicyMixin, OnlyUser


class UserViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes_per_method = {
        'list': [AllowAny],
        'create': [AllowAny],
        'update': [OnlyUser],
        'destroy': [OnlyUser],
        'retrieve': [IsAdminUser, IsAuthenticated]
    }


class PostViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes_per_method = {
        'list': [AllowAny],
        'create': [IsAuthenticated],
        'update': [OnlyUser],
        'destroy': [OnlyUser],
        'retrieve': [AllowAny]
    }


class CommentViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes_per_method = {
        'list': [AllowAny],
        'create': [IsAuthenticated],
        'update': [OnlyUser],
        'destroy': [OnlyUser],
        'retrieve': [AllowAny]
    }
