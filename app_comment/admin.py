from django.contrib import admin
from .models import Comments


# Register your models here.
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'with_article', 'user_name', 'email', 'date', 'text']


admin.site.register(Comments, CommentsAdmin)
