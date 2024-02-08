from django.contrib import admin

from . import models 

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'date', 'like_count', 'view_count')
    list_filter = ('genre', 'date')
    search_fields = ('title', 'author', 'genre', 'date', 'keywords')
    readonly_fields = ('like_count', 'view_count', 'created_at', 'updated_at')
    sortable_by = ('title', 'author', 'genre', 'date', 'like_count', 'view_count')

admin.site.register(models.Article, ArticleAdmin)