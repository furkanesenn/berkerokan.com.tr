from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False, null=False, verbose_name='Başlık')
    description = models.TextField(blank=False, null=False, verbose_name='Açıklama')
    cover = models.ImageField(upload_to='album_images/', blank=False, null=False, verbose_name='Kapak Fotoğrafı')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')  
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')   

    view_count = models.IntegerField(default=0, editable=False, verbose_name='Görüntülenme Sayısı')
    engagement_count = models.IntegerField(default=0, editable=False, verbose_name='Etkileşim Sayısı')

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f'<Album {self.title}>'
    
    def get_absolute_url(self):
        return f'/gallery/albums/{self.id}/'
    
    def view(self):
        self.view_count += 1
        self.save() 

    def engagement(self):
        self.engagement_count += 1
        self.save()

    class Meta:
        verbose_name = 'Albüm'
        verbose_name_plural = 'Albümler'
        ordering = ['-created_at']

class Photo(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False, null=False, verbose_name='Başlık')
    description = models.TextField(blank=False, null=False, verbose_name='Açıklama')

    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos', verbose_name='Albüm') 
    # on_delete=models.CASCADE means that when the album is deleted, all the photos in the album will be deleted as well
    # related_name='photos' is used to access the photos of an album from the album object with the related name

    image = models.ImageField(upload_to='photos/', blank=False, null=False, verbose_name='Fotoğraf')

    date = models.DateField(blank=True, null=True, verbose_name='Tarih')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')

    view_count = models.IntegerField(default=0, editable=False, verbose_name='Görüntülenme Sayısı')

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f'<Photo {self.title}>'
    
    def view(self):
        self.view_count += 1
        self.save()

    class Meta:
        verbose_name = 'Fotoğraf'
        verbose_name_plural = 'Fotoğraflar'
        ordering = ['-created_at']