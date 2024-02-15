from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor.fields import RichTextField

from comments.models import Comment
from newsletter.utils import email
from newsletter.models import Subscriber, Post, Newsletter

class Book(models.Model):
  id = models.AutoField(primary_key=True,)
  title = models.CharField(max_length=200, unique=True, blank=False, null=False, verbose_name='Ad')
  author = models.CharField(max_length=200, blank=False, null=False, default="Berker Okan", verbose_name='Yazar')
  # description = models.TextField(blank=True, null=True, verbose_name='Açıklama')
  description = RichTextField(blank=True, null=True, verbose_name='Açıklama')
  cover = models.ImageField(upload_to='covers/', blank=False, null=False, verbose_name='Kapak Fotoğrafı')
  genre = models.CharField(max_length=200, blank=True, null=True, verbose_name='Tür')
  date = models.DateField(blank=True, null=True, verbose_name='Yayın Tarihi')
  keywords = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anahtar Kelimeler')
  
  price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Fiyat')
  purchase_link = models.URLField(max_length=200, blank=True, null=True, verbose_name='Satın Alma Linki')

  highlight_book = models.BooleanField(default=False, verbose_name='Öne Çıkan Kitap')
  send_email_to_subscribers = models.BooleanField(default=False, verbose_name='Abonelere E-Posta Gönder')
  highlight_email_subject = models.CharField(max_length=200, blank=True, null=True, verbose_name='Öne Çıkan E-Posta Konusu')
  highlight_email_content = models.TextField(blank=True, null=True, verbose_name='Öne Çıkan E-Posta İçeriği')

  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')

  view_count = models.IntegerField(default=0, editable=False, verbose_name='Görüntülenme Sayısı')
  engagement_count = models.IntegerField(default=0, editable=False, verbose_name='Etkileşim Sayısı')

  rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0, editable=False, verbose_name='Değerlendirme (Site İçi)')
  rating_count = models.IntegerField(default=0, editable=False, verbose_name='Değerlendirme Sayısı (Site İçi)')

  comments = GenericRelation(Comment, related_query_name='book')

  def __str__(self):
    return self.title 
  
  def __repr__(self):
    return f'<Book {self.title}>'
  
  def get_absolute_url(self):
    return f'/books/{self.id}/'
  
  def view(self):
    self.view_count += 1
    self.save()

  def engage(self):
    self.engagement_count += 1
    self.save()

  def rate(self, rating, old_rating = 0):
    if old_rating == 0:
      self.rating = ((float(self.rating) * self.rating_count + rating) - old_rating) / (self.rating_count + 1)
      self.rating_count += 1
    else:
      self.rating = ((float(self.rating) * self.rating_count + rating) - old_rating) / (self.rating_count)
    self.save()

  def save(self, *args, **kwargs):
    if not self.id:
      if self.genre == '':
        self.genre = 'Diğer'
      if self.description == '':
        self.description = self.title + ' kitabı hakkında bilgi edinmek için tıklayın.'
        
    super().save(*args, **kwargs)

  class Meta:
    verbose_name = 'Kitap'
    verbose_name_plural = 'Kitaplar'
    ordering = ['-created_at']