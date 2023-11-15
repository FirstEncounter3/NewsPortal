from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import (
    Post,
    Category,
)
from .filters import PostFilter
from .forms import NewsForm

from django.core.cache import cache


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

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)

        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
            return obj


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


class CategoryList(ListView):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_list'
    paginate_by = 10

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Подписка оформлена'
    return render(request, 'subscribe.html', {'category': category, 'message': message})


@login_required
def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.remove(user)

    message = 'Подписка отменена'
    return render(request, 'subscribe.html', {'category': category, 'message': message})


@login_required
def subscribe_list(request):
    user = request.user
    category = Category.objects.filter(subscribers=user.id)

    print(user.username)
    print(category)

    message = 'Ваши подписки'
    return render(request, 'subscribe_list.html', {'category': category, 'message': message})
