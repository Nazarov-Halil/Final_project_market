from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.blog.models import Blog


class BlogList(ListView):
    model = Blog
    template_name = 'shop-full-width.html'
    context_object_name = 'blog'

    def get_queryset(self):
        return Blog.objects.all()


class BlogDetail(DetailView):
    queryset = Blog.objects.all()
    template_name = 'product-full-width.html'
    context_object_name = 'object'

