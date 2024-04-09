# Generated by Django 5.0.4 on 2024-04-04 09:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Карзина',
                'verbose_name_plural': 'Карзины',
            },
        ),
        migrations.CreateModel(
            name='CartBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='Каличество')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to='blog.blog', verbose_name='Продукт')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_cart', to='cart.cart', verbose_name='Карзина')),
            ],
            options={
                'verbose_name': 'Элемент Карзина',
                'verbose_name_plural': 'Элемент Карзины',
            },
        ),
    ]