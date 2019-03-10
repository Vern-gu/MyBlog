from django.shortcuts import render, redirect, get_object_or_404
from app_blog.models import *
from .models import Comments
from .forms import CommentForm


def article_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.with_article = article
            comment.save()
            return redirect(article)
            # 当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
        else:
            comment_list = article.comments_set.filter(isDelete=False)
            # 等价于 Comments.objects.filter(with_article=article)
            context = {
                'article': article,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blog/detail.html', context=context)
    return redirect(article)
