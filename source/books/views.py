from django.shortcuts import render, redirect

from . import models
from core.utils import search_engine, session_manager

"""
TODOS:

- Engagement and view count should be updated when a user interacts with the book object. - Done
- Comment and rating system should be implemented for books. - Done
- Highlight new books in the books list view. Also send an email to the subscribers when a new book is added. - Done
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
    book = models.Book.objects.get(id=id)
    book.view()
    return render(request, 'book_detail.html', {"book": book}, status=200) 

# Rate book view

def book_rate(request, id):
    if request.method != 'POST':
        return redirect('books:book-detail', id=id)
    
    book = models.Book.objects.get(id=id)
    
    if book is None:
        return redirect('books:book-detail', id=id)

    rating = int(request.POST.get('rating'))

    if rating < 1 or rating > 5:
        return redirect('books:book-detail', id=id)

    session = session_manager.SessionManager(request)

    old_rating = session.get(f'book_{id}_rating') or 0
    session.set(f'book_{id}_rating', rating)

    book.rate(rating, old_rating)
    book.engage()

    return redirect('books:book-detail', id=id)

