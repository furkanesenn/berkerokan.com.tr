from django.db import models

from newsletter.utils import hash, email

class Newsletter(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Bülten Adı')
    description = models.TextField(blank=True, null=True, verbose_name='Açıklama')

    verification_email_subject = models.CharField(max_length=100, blank=True, null=True, verbose_name='Doğrulama E-Posta Konusu')
    verification_email_content = models.TextField(blank=True, null=True, verbose_name='Doğrulama E-Posta İçeriği')

    welcome_email_subject = models.CharField(max_length=100, blank=True, null=True, verbose_name='Hoşgeldiniz E-Posta Konusu')
    welcome_email_content = models.TextField(blank=True, null=True, verbose_name='Hoşgeldiniz E-Posta İçeriği')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    last_posted_at = models.DateTimeField(blank=True, null=True, editable=False, verbose_name='Son Gönderi Tarihi')

    active = models.BooleanField(default=True, verbose_name='Aktif')

    subscriber_count = models.IntegerField(default=0, null=True, blank=True, editable=False, verbose_name='Abone Sayısı')
    confirmed_subscriber_count = models.IntegerField(default=0, null=True, blank=True, editable=False, verbose_name='Onaylanmış Abone Sayısı')
    newsletter_stats = models.JSONField(blank=True, null=True, editable=False, verbose_name='Bülten İstatistikleri')

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'<Newsletter: {self.name}>'
    
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'newsletters'
        ordering = ['created_at']
        verbose_name = 'Bülten'
        verbose_name_plural = 'Bültenler'

class Subscriber(models.Model):
    id = models.AutoField(primary_key=True)

    email = models.EmailField(unique=True, blank=False, null=False, verbose_name='E-Posta Adresi')
    first_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ad')
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Soyad')

    subscribed_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Abonelik Tarihi')
    unsubscribed_at = models.DateTimeField(blank=True, null=True, editable=False, verbose_name='Abonelikten Ayrılma Tarihi')

    subscription_confirmed = models.BooleanField(default=False, editable=False, verbose_name='Abonelik Onayı')
    subscription_status = models.BooleanField(default=True, editable=False, verbose_name='Abonelik Durumu')
    subscription_token = models.CharField(max_length=1000, blank=True, null=True, editable=False, default=hash.create_hash, verbose_name='Abonelik Doğrulama Kodu')

    received_email_count = models.IntegerField(default=0, editable=False, verbose_name='Alınan E-Posta Sayısı')

    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='subscribers', verbose_name='Bülten')

    def __str__(self):
        return self.email
    
    def __repr__(self):
        return f'<Subscriber: {self.email}>'
    
    def __unicode__(self):
        return self.email

    class Meta:
        db_table = 'subscribers'
        ordering = ['subscribed_at']
        verbose_name = 'Abone'
        verbose_name_plural = 'Aboneler'

class Post(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Başlık')
    content = models.TextField(blank=False, null=False, verbose_name='İçerik')

    published_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Yayınlanma Tarihi')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name='Güncellenme Tarihi')

    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='posts', verbose_name='Bülten')

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f'<Post: {self.title}>'
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.newsletter.last_posted_at = self.published_at
            self.newsletter.save()
            
            email.send_custom_email(self.newsletter.subscribers.all(), self)

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'posts'
        ordering = ['-published_at']
        verbose_name = 'Gönderi'
        verbose_name_plural = 'Gönderiler'