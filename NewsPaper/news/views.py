from django.views.generic import ListView, DetailView
from .models import Post


class ArticlesList(ListView):
    model = Post
    ordering = '-created_at'
    template_name = 'articles.html'
    context_object_name = 'articles'


class ArticleDetail(DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'article'
