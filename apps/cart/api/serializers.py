from rest_framework import serializers
from apps.cart.models import CartBlog, Cart


class CarBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartBlog
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_blog = CarBlogSerializer(
        read_only=True,
        many=True,
    )
    class Meta:
        model = Cart
        fields = '__all__'
