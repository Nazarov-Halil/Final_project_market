from django.urls import path
from apps.blog import views


urlpatterns = [
    path('blog_list/', views.BlogList.as_view(), name='blog_list'),
    path('detail/<int:pk>/', views.BlogDetail.as_view(), name='detail_blog')
]