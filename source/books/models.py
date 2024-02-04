from django.db import models

class Book(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200, unique=True, blank=False, null=False)
  author = models.CharField(max_length=200, blank=False, null=False)
  description = models.TextField(blank=True, null=True)
  cover = models.ImageField(upload_to='covers/', blank=False, null=False)
  genre = models.CharField(max_length=200, blank=True, null=True)
  date = models.DateField(blank=True, null=True)
  keywords = models.CharField(max_length=200, blank=True, null=True)
  
  price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
  purchase_link = models.URLField(max_length=200, blank=True, null=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  view_count = models.IntegerField(default=0, editable=False)
  impression_count = models.IntegerField(default=0, editable=False)

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