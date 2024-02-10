from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from newsletter.utils import hash

class Comment(models.Model):
  id = models.AutoField(primary_key=True)

  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey('content_type', 'object_id')

  author = models.CharField(max_length=200, blank=False, null=False, verbose_name='Yorumun Sahibi')
  author_email = models.EmailField(max_length=200, blank=False, null=False, verbose_name='Yorumun Sahibinin E-Posta Adresi')
  body = models.TextField(blank=False, null=False, verbose_name='Yorumun İçeriği')

  subcomments = GenericRelation('self', related_query_name='sup_comment', verbose_name='Alt Yorumlar')

  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')

  like_count = models.IntegerField(default=0, editable=False, verbose_name='Beğeni Sayısı')
  email_notification = models.BooleanField(default=True, verbose_name='E-Posta Bildirimi')
  report_count = models.IntegerField(default=0, editable=False, verbose_name='Şikayet Sayısı')
  
  access_token = models.CharField(max_length=200, blank=False, null=False, editable=False, default=hash.create_hash, verbose_name='Yorumun Tokeni')

  def __str__(self):
    return f'{self.author} - {self.content_object}'
  
  def __repr__(self):
    return f'<Comment {self.author} - {self.content_object}>'
  
  def like(self):
    self.like_count += 1
    self.save()
    return True
  
  def dislike(self):
    self.like_count -= 1
    self.save()
    return True
  
  def report(self):
    self.report_count += 1
    self.save()
    return True
  
  def unreport(self):
    self.report_count -= 1
    self.save()
    return True
  
  def get_absolute_url(self):
    return f'/{self.content_object._meta.app_label}/{self.object_id}#comment-{self.id}'
  
  class Meta:
    ordering = ['-created_at']
    verbose_name = 'Yorum'
    verbose_name_plural = 'Yorumlar'