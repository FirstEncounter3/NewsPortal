from django.contrib import admin
from .models import (
    Author,
    Category,
    Post,
    Comment,
)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating',)
    list_filter = ('rating',)
    search_fields = ('user__username',)


class CategoryAdmin(admin.ModelAdmin):
    def category_subscribers(self, category):
        return ', '.join([subscribers.username for subscribers in category.subscribers.all()])

    list_display = ('category_name', 'category_subscribers',)
    list_filter = ('category_name',)
    search_fields = ('category_name',)


class PostsAdmin(admin.ModelAdmin):
    def post_category(self, post):
        return ', '.join([category.category_name for category in post.category.all()])

    list_display = ('type', 'heading', 'text', 'created_at', 'author', 'post_category',)
    list_filter = ('created_at', 'type', 'category__category_name',)
    search_fields = ('text', 'heading', 'category__category_name', 'author__user__username',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'text', 'created_at', 'rating',)
    list_filter = ('created_at', 'rating',)
    search_fields = ('post__heading', 'user__username', 'text',)


# Register your models here.

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostsAdmin)
admin.site.register(Comment, CommentAdmin)
