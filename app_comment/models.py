from django.db import models


class Comments(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField(default=False)
    with_article = models.ForeignKey('app_blog.Article', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]

    class Meta:
        db_table = 'comments'

