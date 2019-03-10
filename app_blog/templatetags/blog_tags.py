# 自定义模板标签
from ..models import Article, Category
from django import template

register = template.Library()


@register.simple_tag
def get_recent_article(num=5):
    return Article.objects.filter(isDelete=False).order_by("-date")[:num]


@register.simple_tag
def archives():
    return Article.objects.dates('date', 'month', order='DESC')
# 这里dates方法会返回一个列表，列表中的元素为每一篇文章的创建时间，且是 Python 的 date 对象，精确到月份，降序排列


@register.simple_tag
def get_category():
    return Category.objects.filter(isDelete=False)
