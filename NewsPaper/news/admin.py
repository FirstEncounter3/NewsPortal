from django.contrib import admin
from .models import (
    Author,
    Category,
    Post,
    PostCategory,
    Comment,
)

# Register your models here.

admin.site.register(
    [
        Author,
        Category,
        Post,
        PostCategory,
        Comment,
    ]
)
