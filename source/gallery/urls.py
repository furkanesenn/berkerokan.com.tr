from django.urls import path 

from . import views

app_name = 'gallery'

urlpatterns = [
  path('', views.gallery_albums, name='gallery-albums'),
  path('<int:album_id>', views.gallery_album, name='gallery-album'),
  path('engagement/<int:photo_id>', views.gallery_engagement, name='gallery-engagement')
]