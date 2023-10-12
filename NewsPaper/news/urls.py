from django.urls import path
from .views import ArticlesList, ArticleDetail

urlpatterns = [
    path('', ArticlesList.as_view()),
    path('<int:pk>', ArticleDetail.as_view()),
]
