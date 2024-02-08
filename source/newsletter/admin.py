from django.contrib import admin

from . import models 

class SubscriberInline(admin.TabularInline):
    model = models.Subscriber
    fields = ('email', 'first_name', 'last_name')
    can_delete = False

    max_num = 0
    extra = 0
    show_change_link = True

class PostInline(admin.TabularInline):
    model = models.Post
    fields = ('title',)
    can_delete = False

    max_num = 0
    extra = 0
    show_change_link = True


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'subscriber_count', 'confirmed_subscriber_count', 'last_posted_at', 'active')
    list_filter = ('created_at', 'active')
    search_fields = ('name', 'created_at')
    readonly_fields = ('subscriber_count', 'confirmed_subscriber_count', 'newsletter_stats', 'created_at', 'last_posted_at')
    sortable_by = ('name', 'created_at', 'subscriber_count', 'confirmed_subscriber_count', 'last_posted_at', 'active')
    inlines = [SubscriberInline, PostInline]

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'subscribed_at', 'unsubscribed_at', 'subscription_confirmed', 'subscription_status', 'received_email_count')
    list_filter = ('subscribed_at', 'unsubscribed_at', 'subscription_confirmed', 'subscription_status')
    search_fields = ('email', 'first_name', 'last_name', 'subscribed_at', 'unsubscribed_at')
    readonly_fields = ('subscribed_at', 'unsubscribed_at', 'subscription_confirmed', 'subscription_status', 'subscription_token', 'received_email_count')
    sortable_by = ('email', 'subscribed_at', 'unsubscribed_at', 'subscription_confirmed', 'subscription_status', 'received_email_count')
    list_select_related = ('newsletter',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'newsletter', 'updated_at')
    list_filter = ('published_at', 'newsletter', 'updated_at')
    search_fields = ('title', 'published_at', 'newsletter', 'updated_at')
    readonly_fields = ('published_at', 'updated_at')
    sortable_by = ('title', 'published_at', 'newsletter', 'updated_at')
    list_select_related = ('newsletter',)

admin.site.register(models.Newsletter, NewsletterAdmin)
admin.site.register(models.Subscriber, SubscriberAdmin)
admin.site.register(models.Post, PostAdmin)