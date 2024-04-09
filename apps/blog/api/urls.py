from rest_framework.routers import DefaultRouter

from apps.blog.api import views
from apps.cart.api.views import CartAPIView
router = DefaultRouter()
router.register('blog', views.BlogViewSet, basename="blog_api")
router.register('tag', views.BlogTagAPIViewSet, basename='blog_tag')
router.register('like', views.BlogLikeAPIViewSet, basename='blog_like')
router.register('image', views.BlogImageAPIViewSet, basename='blog_image')
# router.register('comment', CommentAPIViewSet, basename='blog_comment')
router.register('cart', CartAPIView, basename='cart')

urlpatterns = [

]
urlpatterns += router.urls
