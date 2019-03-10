from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from app_comment.forms import CommentForm
from django.views.generic import ListView


# Create your views here.
class IndexView(ListView):
    model = Article
    template_name = 'blog/blog_list.html'
    context_object_name = 'articles'
    # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 1

    def get_queryset(self):
        return super(IndexView, self).get_queryset().filter(isDelete=False)


def index(request):
    return render(request, 'index.html')


# def blog_list(request):  使用通用的类视图ListView代替
#     article_list = Article.objects.filter(isDelete=False)
#     context = {
#             'articles': article_list,
#             }
#     return render(request, 'blog/blog_list.html', context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 其作用就是当传入的 pk 对应的 Post 在数据库存在时，就返回对应的 post，如果不存在，
    # 就给用户返回一个 404 错误，表明用户请求的文章不存在。
    article.increase_views()
    form = CommentForm
    comment_list = article.comments_set.filter(isDelete=False)
    context = {
        'article': article,
        'form': form,
        'comment_list': comment_list,
    }
    return render(request, 'blog/detail.html', context)


def archives(request, year, month):
    article_list = Article.objects.filter(isDelete=False,
                                          date__year=year,
                                          date__month=month,
                                          )
    context = {'articles': article_list}
    return render(request, 'blog/blog_list.html', context)


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(isDelete=False,
                                          category=cate)
    context = {'articles': article_list}
    return render(request, 'blog/blog_list.html', context)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')



