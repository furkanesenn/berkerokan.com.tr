from django.db import models

class Book(models.Model):
  id = models.AutoField(primary_key=True,)
  title = models.CharField(max_length=200, unique=True, blank=False, null=False, verbose_name='Ad')
  author = models.CharField(max_length=200, blank=False, null=False, verbose_name='Yazar')
  description = models.TextField(blank=True, null=True, verbose_name='Açıklama')
  cover = models.ImageField(upload_to='covers/', blank=False, null=False, verbose_name='Kapak Fotoğrafı')
  genre = models.CharField(max_length=200, blank=True, null=True, verbose_name='Tür')
  date = models.DateField(blank=True, null=True, verbose_name='Yayın Tarihi')
  keywords = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anahtar Kelimeler')
  
  price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Fiyat')
  purchase_link = models.URLField(max_length=200, blank=True, null=True, verbose_name='Satın Alma Linki')

  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')

  view_count = models.IntegerField(default=0, editable=False, verbose_name='Görüntülenme Sayısı')
  engagement_count = models.IntegerField(default=0, editable=False, verbose_name='Etkileşim Sayısı')

  def __str__(self):
    return self.title 
  
  def __repr__(self):
    return f'<Book {self.title}>'
  
  def get_absolute_url(self):
    return f'/books/{self.id}/'
  
  def view(self):
    self.view_count += 1
    self.save()

  def impression(self):
    self.impression_count += 1
    self.save()

  class Meta:
    verbose_name = 'Kitap'
    verbose_name_plural = 'Kitaplar'
    ordering = ['-created_at']