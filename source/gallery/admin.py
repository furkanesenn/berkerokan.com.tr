from django.contrib import admin

from . import models 

class PhotoInline(admin.TabularInline):
    model = models.Photo
    fields = ('title', 'image')
    can_delete = False

    max_num = 0
    extra = 0
    show_change_link = True

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'engagement_count', 'view_count')
    list_filter = ('created_at',)
    search_fields = ('title', 'created_at', 'keywords')
    readonly_fields = ('engagement_count', 'view_count', 'created_at', 'updated_at')
    sortable_by = ('title', 'created_at', 'engagement_count', 'view_count')
    inlines = [PhotoInline]

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'view_count', 'album')
    list_filter = ('created_at', 'album')
    search_fields = ('title', 'created_at', 'keywords', 'album__name')
    readonly_fields = ('view_count', 'created_at', 'updated_at')
    sortable_by = ('title', 'created_at', 'view_count')
    list_select_related = ('album',) 

admin.site.register(models.Album, AlbumAdmin)
admin.site.register(models.Photo, PhotoAdmin)