from django.urls import path
from apps.main import views

urlpatterns = [
    path('', views.TemplateView.as_view(), name='main')
]