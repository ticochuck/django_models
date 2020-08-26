from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from .models import Post

# Create your views here.

class HomePage(ListView):
    template_name = 'home.html'
    model = Post


class PostDetailPage(DetailView):
    template_name = 'post_detail.html'
    model = Post