from django.contrib import admin  
from django.contrib.contenttypes.admin import GenericTabularInline
from . import models

class CommentInline(GenericTabularInline):
  model = models.Comment
  fields = ('author', 'body', 'like_count', 'report_count')
  readonly_fields = ('like_count', 'report_count')
  can_delete = False

  max_num = 0
  extra = 0
  show_change_link = True

admin.site.register(models.Comment)