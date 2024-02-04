from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    cover = models.ImageField(upload_to='album_images/', blank=False, null=False)
    
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)   

    view_count = models.IntegerField(default=0, editable=False)
    impression_count = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f'<Album {self.title}>'
    
    def get_absolute_url(self):
        return f'/gallery/albums/{self.id}/'
    
    def view(self):
        self.view_count += 1
        self.save() 

    def impression(self):
        self.impression_count += 1
        self.save()

class Photo(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos') 
    # on_delete=models.CASCADE means that when the album is deleted, all the photos in the album will be deleted as well
    # related_name='photos' is used to access the photos of an album from the album object with the related name

    image = models.ImageField(upload_to='photos/', blank=False, null=False)

    date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    view_count = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f'<Photo {self.title}>'
    
    def view(self):
        self.view_count += 1
        self.save()