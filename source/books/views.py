from django.shortcuts import render

from . import models
from core.utils import search_engine

"""
TODOS:

- Engagement and view count should be updated when a user interacts with the book object.
- Comment and rating system should be implemented for books.
- Highlight new books in the books list view. Also send an email to the subscribers when a new book is added.
"""

# All books view 

def books_list(request):
    
    books = models.Book.objects.all()

    if len(books) == 0:
        return render(request, 'books_list.html', {"message": "No book object found.", "books": None, "genres": None, "years": None}, status=404)
    
    all_genres = models.Book.objects.values_list('genre', flat=True).distinct() # Get all unique genres
    all_years = map(lambda x: x.year, models.Book.objects.values_list('date', flat=True).distinct()) # Get all unique years 
    # values_list: Returns a QuerySet that returns dictionaries, rather than model instances, when used as an iterable.
    # flat: If True, this will be a flat list of single values instead of a list of one-tuples.
    # distinct: Returns a new QuerySet that uses SELECT DISTINCT in its SQL query.
    books, _ = search_engine.sort("a-z", books)
    return render(request, 'books_list.html', {"books": books, "genres": all_genres, "years": all_years}, status=200)

# Search view 

def book_search(request):
    search_result = search_engine.search(request, models.Book, 'books')
    return render(request, 'books_list.html', search_result['data'], status=search_result['status'])

# Book detail view 
    
def book_detail(request, id):
    return render(request, 'book_detail.html', {"book": models.Book.objects.get(id=id)}, status=200) 