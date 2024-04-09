from rest_framework import viewsets
from apps.cart.api import serializers

from apps.cart.models import CartBlog, Cart


class CartAPIView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.CarBlogSerializer
        elif self.action in ['destroy']:
            return None
        return self.serializer_class
