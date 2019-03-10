from django.urls import path, re_path
from app_blog.views import *


# app_name='blog'或者在子url文件内定义命名空间
urlpatterns = [
    path('', IndexView.as_view(), name='blog_list'),
    re_path(r'^(?P<pk>\d+)/$', detail, name='detail'),
    re_path(r'^archives/(?P<year>\d{4})/(?P<month>\d{1,2})/$', archives, name='archives'),
    re_path(r'category/(?P<pk>\d+)/$', category, name='category'),
]
