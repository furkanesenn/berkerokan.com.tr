from django.db import models

ARTICLE_TYPES = (
    ('Dizi Hikayeler', 'Dizi Hikayeler'),
    ('Öyküler', 'Öyküler'),
    ('Denemeler', 'Denemeler'),
    ('Kaynak Tavsiyeleri', 'Kaynak Tavsiyeleri'),
    ('Kitap Yorumları', 'Kitap Yorumları'),
)

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True, blank=False, null=False, verbose_name='Başlık')
    body = models.TextField(blank=False, null=False, verbose_name='İçerik')
    short_description = models.TextField(blank=False, null=False, verbose_name='Kısa Açıklama')
    genre = models.CharField(max_length=200, choices=ARTICLE_TYPES, default='Dizi Hikayeler', blank=False, null=False, verbose_name='Tür')
    keywords = models.CharField(max_length=200, blank=False, null=False, verbose_name='Anahtar Kelimeler')

    author = models.CharField(max_length=200, blank=False, null=False, verbose_name='Yazar')
    
    cover = models.ImageField(upload_to='article_images/', blank=False, null=False, verbose_name="Kapak Fotoğrafı") # upload_to specifies the directory to which the file is uploaded

    date = models.DateField(auto_now_add=True, verbose_name="Yazılma Tarihi") # auto_now=False and auto_now_add=False means that the field is not automatically updated

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi") # auto_now_add will set the value of the field to current datetime when the object is first created
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi") # auto_now will set the value of the field to current datetime every time the object is saved

    like_count = models.IntegerField(default=0, editable=False, verbose_name="Beğeni Sayısı") # editable=False means that the field is not editable in the admin interface
    view_count = models.IntegerField(default=0, editable=False, verbose_name="Görüntülenme Sayısı") # editable=False means that the field is not editable in the admin interface

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f'<Article {self.title}>'

    def get_absolute_url(self):
        return f'/articles/{self.id}/'

    def like(self):
        self.like_count += 1
        self.save()
        return True 
    
    def dislike(self):
        self.like_count -= 1
        self.save()
        return True

    def view(self):
        self.view_count += 1
        self.save()
        return True 
    
    class Meta:
        verbose_name = "Yazı"
        verbose_name_plural = "Yazılar"
        db_table = 'articles'
        ordering = ['-date']