from django.shortcuts import render, redirect

from . import models

"""
TODOS:

- Make the URLS Turkish
- Create stats page for albums and photos
- Import and export to the admin panel

"""

# All albums view

def gallery_albums(request):
    albums = models.Album.objects.all()

    if len(albums) == 0:
        return render(request, 'gallery_albums.html', {"message": "No album object found.", "albums": None}, status=404)
    
    return render(request, 'gallery_albums.html', {"albums": albums}, status=200)

# Single album view

def gallery_album(request, album_id: int):
    album = models.Album.objects.get(id=album_id)

    if album is None:
        return render(request, 'gallery_album.html', {"message": "Album not found.", "album": None}, status=404)
    
    album.view()
    return render(request, 'gallery_album.html', {"album": album}, status=200)

# Photo engagement view

def gallery_engagement(request, photo_id: int):
    photo = models.Photo.objects.get(id=photo_id)

    if photo is None:
        return redirect('gallery-album', album_id=photo.album.id)
    
    photo.album.engagement()
    photo.view()

    return redirect('gallery-album', album_id=photo.album.id)