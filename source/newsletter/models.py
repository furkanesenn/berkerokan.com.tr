from django.db import models

class Subscriber(models.Model):
    id = models.AutoField(primary_key=True)

    email = models.EmailField(unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    subscribed_at = models.DateTimeField(auto_now_add=True)
    unsubscribed_at = models.DateTimeField(blank=True, null=True)

    received_email_count = models.IntegerField(default=0)

    def __str__(self):
        return self.email
    
    def __repr__(self):
        return f'<Subscriber: {self.email}>'
    
    def __unicode__(self):
        return self.email

    class Meta:
        db_table = 'subscribers'
        ordering = ['subscribed_at']

class Post(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False, null=False)

    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f'<Post: {self.title}>'
    
    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'posts'
        ordering = ['-published_at']