from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .filters import PostFilter
from .forms import NewsForm


class ArticlesList(ListView):
    model = Post
    ordering = '-created_at'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 10


class ArticleDetail(DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'article'


class ArticlesSearch(ListView):
    model = Post
    ordering = '-created_at'
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class NewsCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = NewsForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'Ns'
        return super().form_valid(form)


class NewsEdit(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('articles_list')


class ArticleCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = NewsForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'article_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'Ae'
        return super().form_valid(form)


class ArticleEdit(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'article_create.html'


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('articles_list')
