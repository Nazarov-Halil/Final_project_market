from rest_framework import serializers
from apps.blog.models import Blog, BlogImage, BlogTag, BlogLike
from apps.cart.models import Cart
from apps.cart.api.serializers import CartSerializer

class CartBLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = '__all__'


class BlogLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogLike
        fields = '__all__'


class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = '__all__'


class BLogSerializer(serializers.ModelSerializer):
    image = BlogImageSerializer(
        read_only=True,
        many=True,
    )
    tag = BlogTagSerializer(
        read_only=True,
        many=True
    )
    total_likes = serializers.SerializerMethodField()
    cart = CartBLogSerializer(
        read_only=True,
        many=True
    )
    class Meta:
        model = Blog
        fields = '__all__'

    def get_total_likes(self, instance):
        return instance.like.all().count()

class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class BlogImageUpdateRetrieveDestroy(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = ['image']
