from django.urls import path 

from . import views

urlpatterns = [
  path('', views.gallery_albums, name='gallery-albums'),
  path('<int:album_id>', views.gallery_album, name='gallery-album'),
  path('impression/<int:photo_id>', views.gallery_impression, name='gallery-impression')
]