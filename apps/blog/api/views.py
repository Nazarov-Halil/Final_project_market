from rest_framework import viewsets, generics

from apps.blog.api import serializers
from apps.blog.models import BlogTag, Blog, BlogLike, BlogImage
from apps.cart.models import CartBlog

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = serializers.BLogSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.BlogCreateSerializer
        elif self.action in ['update']:
            return serializers.BlogCreateSerializer
        elif self.action in ['destroy']:
            return None
        return self.serializer_class


class BlogImageAPIViewSet(viewsets.ModelViewSet):
    queryset = BlogImage.objects.all()
    serializer_class = serializers.BlogImageSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.BlogImageSerializer
        elif self.action in ['update']:
            return serializers.BlogImageUpdateRetrieveDestroy
        elif self.action in ['destroy']:
            return None
        return self.serializer_class


class BlogLikeAPIViewSet(viewsets.ModelViewSet):
    queryset = BlogLike.objects.all()
    serializer_class = serializers.BlogLikeSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.BlogLikeSerializer
        elif self.action in ['destroy']:
            return None
        return self.serializer_class


class BlogTagAPIViewSet(viewsets.ModelViewSet):
    queryset = BlogTag.objects.all()
    serializer_class = serializers.BlogTagSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return self.serializer_class
        elif self.action in ['update']:
            return self.serializer_class
        elif self.action in ['destroy']:
            return None
        return self.serializer_class


class BlogCartAPIView(viewsets.ModelViewSet):
    queryset = CartBlog.objects.all()
    serializer_class = serializers.CartSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.CartSerializer
        elif self.action in ['destroy']:
            return None
        return self.serializer_class
