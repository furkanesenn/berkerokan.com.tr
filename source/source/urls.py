from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('articles/', include('articles.urls')),
    path('gallery/', include('gallery.urls')),
    path('', include('core.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)