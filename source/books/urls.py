from django.urls import path 

from . import views 

urlpatterns = [
  path('', views.books_list, name='books-list'),
  path('s', views.book_search, name='book-search'),
  path('<int:id>', views.book_detail, name='book-detail'),
]