from django.db import models
from apps.blog.models import Blog
from django.contrib.auth import get_user_model

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='Пользователь'
    )

    def get_total_sum(self):
        return sum(i.get_subtotal_sum() for i in self.items_cart .all())

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Карзина'
        verbose_name_plural = 'Карзины'


class CartBlog(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE,
        related_name='cart_item',
        verbose_name='Продукт'
    )
    quantity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Каличество'
    )
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE,
        related_name='items_cart',
        verbose_name='Карзина'
    )

    def get_subtotal_sum(self):
        return int(self.quantity * self.blog.price)

    def __str__(self):
        return self.blog.title

    class Meta:
        verbose_name = 'Элемент Карзина'
        verbose_name_plural = 'Элемент Карзины'
