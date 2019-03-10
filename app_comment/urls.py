from django.urls import path, re_path
from .views import *


app_name = 'comments'
urlpatterns = [
    re_path(r'^article/(?P<article_pk>\d+)/$', article_comment, name='article_comment')
]
