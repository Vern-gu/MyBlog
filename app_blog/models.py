from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = '分类'


class Article(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    abstract = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})  # url的反向解析，通过地址来获取url

    class Meta:
        db_table = '文章信息'
        ordering = ['-date']



