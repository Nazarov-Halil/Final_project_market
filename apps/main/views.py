from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class MainTemplate(ListView):
    template_name = 'index.html'
