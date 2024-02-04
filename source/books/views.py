from django.shortcuts import render

from . import models

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
    return render(request, 'books_list.html', {"books": sort(books, "a-z"), "genres": all_genres, "years": all_years}, status=200)

# Search view 

def search(request):
    if not request.GET:
        return render(request, 'books_list.html', {"message": "You have to use the GET method for this path."}, status=403)
    
    filtered_objects = models.Book.objects.all()
    genre = year = sorting = None
    if 'genre' in request.GET:
        filtered_objects, genre = filter(request, 'genre')

    if 'year' in request.GET:
        filtered_objects, year = filter(request, 'year', prefiltered=filtered_objects)

    if 'sort' in request.GET:
        filtered_objects, sorting = sort(filtered_objects, request.GET.get('sort'))

    search_query = request.GET.get('search-query', None)
    search_query = search_query.strip()

    if search_query is None: 
        return render(request, 'books_list.html', {"message": "No search query provided."}, status=403)
    
    books = filtered_objects.filter(title__icontains=search_query)
    books |= filtered_objects.filter(keywords__icontains=search_query) # Union of two querysets

    all_genres = models.Book.objects.values_list('genre', flat=True).distinct()
    all_years = set(map(lambda x: x.year, models.Book.objects.values_list('date', flat=True).distinct()))
    if len(books) == 0:  
        return render(request, 'books_list.html', {"message": "No book object found.", "books": None, "genres": all_genres, "fgenre": genre, "years": all_years, "fyear": year, "sorting": sorting, "search_query": search_query}, status=404)
    
    return render(request, 'books_list.html', {"books": books, "genres": all_genres, "fgenre": genre, "years": all_years, "fyear": year, "sorting": sorting, "search_query": search_query}, status=200)

# Filter view 

def filter(request, field, prefiltered=models.Book.objects.all()):
    if field == "genre":
      curr_genre = request.GET.get('genre')
      return prefiltered.filter(genre=curr_genre), curr_genre
    elif field == "year":
      curr_year = request.GET.get('year')
      return prefiltered.filter(date__icontains=curr_year), curr_year
    else: 
      return prefiltered, None
    
# Sorting view 
    
def sort(prefiltered = models.Book.objects.all(), field = "a-z"):
    if field == "date":
        return prefiltered.order_by('date').reverse(), field 
    elif field == "a-z":
        return prefiltered.order_by('title'), field 
    else: 
        return prefiltered, None
    
# Book detail view 
    
def book_detail(request, id):
    return render(request, 'book_detail.html', {"book": models.Book.objects.get(id=id)}, status=200) 