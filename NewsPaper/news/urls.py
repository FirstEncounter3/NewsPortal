from django.urls import path
from .views import (
    ArticlesList,
    ArticleDetail,
    ArticlesSearch,
    NewsCreate,
    NewsEdit,
    NewsDelete,
    ArticleCreate,
    ArticleEdit,
    ArticleDelete,
    CategoryList,
    subscribe,
    unsubscribe,
    subscribe_list,
)
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(1)(ArticlesList.as_view()), name='articles_list'),
    path('<int:pk>', cache_page(60*5)(ArticleDetail.as_view()), name='article_detail'),
    path('search/', ArticlesSearch.as_view(), name='articles_search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('categories/<int:pk>', CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
    path('categories/<int:pk>/unsubscribe', unsubscribe, name='unsubscribe'),
    path('subscriptions/', subscribe_list, name='subscriptions')

]
