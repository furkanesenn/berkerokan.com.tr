from django.contrib import admin

from . import models 
from comments.admin import CommentInline

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'date', 'engagement_count', 'view_count', 'rating', 'created_at', 'updated_at', 'send_email_to_subscribers', 'highlight_book')
    list_filter = ('genre', 'date', 'send_email_to_subscribers', 'highlight_book')
    search_fields = ('title', 'author', 'genre', 'date', 'keywords', )
    readonly_fields = ('engagement_count', 'view_count', 'created_at', 'updated_at', 'rating', 'rating_count')
    sortable_by = ('title', 'author', 'genre', 'date', 'engagement_count', 'view_count', 'rating')
    inlines = [CommentInline]

admin.site.register(models.Book, BookAdmin)