from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


# Create your models here.

class Author(models.Model):
    rating = models.IntegerField(default=0)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}, rating: {self.rating}'

    def update_rating(self):
        post_rating = self.post_set.aggregate(post_rating=Sum('rating'))
        intermediate_post_rating = 0
        intermediate_post_rating += post_rating.get('post_rating')

        comment_rating = self.user.comment_set.aggregate(comment_rating=Sum('rating'))
        intermediate_comment_rating = 0
        intermediate_comment_rating += comment_rating.get('comment_rating')

        self.rating = intermediate_post_rating * 3 + intermediate_comment_rating
        self.save()


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return f'{self.category_name}'


class Post(models.Model):
    article = 'Ae'
    news = 'Ns'

    TYPES = [(article, "Статья"), (news, "Новость")]

    type = models.CharField(max_length=2, choices=TYPES, default=article)
    created_at = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    category = models.ManyToManyField(Category, through='PostCategory')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.heading}, Автор: {self.author}, Вид: {self.type}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[0:124]}... '

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category} - {self.post}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user} - {self.post}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


# class Subscriber(models.Model):
#     user = models.ForeignKey(
#         to=User,
#         on_delete=models.CASCADE,
#         related_name='subscriber',
#     )
#     category = models.ForeignKey(
#         to='Category',
#         on_delete=models.CASCADE,
#         related_name='subscriber',
#     )
