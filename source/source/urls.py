from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls'), name='books'),
    path('articles/', include('articles.urls'), name='articles'),
    path('gallery/', include('gallery.urls'), name='gallery'),
    path('newsletter/', include('newsletter.urls'), name='newsletter'),
    path('comments/', include('comments.urls'), name='comments'),
    path('', include('core.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)