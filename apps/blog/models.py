from django.db import models
from utils import image_blog
import os


class BlogTag(models.Model):
    title = models.CharField(max_length=100, )

    def __str__(self):
        return self.id


class Blog(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",

    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создание",
    )

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='blog_image',
        verbose_name='Продукт'
    )
    blog_image = models.ImageField(
        upload_to=image_blog.upload_products,
        verbose_name='Картинка'
    )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.blog_image.path)
        super().delete(using=None, keep_parents=False)

    def __str__(self):
        return f'{self.blog_image.url}'


class BlogLike(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='like'
    )
