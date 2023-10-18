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
)

urlpatterns = [
    path('', ArticlesList.as_view(), name='articles_list'),
    path('<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('search/', ArticlesSearch.as_view(), name='articles_search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]
