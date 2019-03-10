from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'user', 'category']


admin.site.register(Category)
admin.site.register(Article,ArticleAdmin)
