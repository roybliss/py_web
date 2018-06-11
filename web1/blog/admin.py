from django.contrib import admin
from .models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_time')
    list_filter = ('create_time', )

admin.site.register(Article, ArticleAdmin)