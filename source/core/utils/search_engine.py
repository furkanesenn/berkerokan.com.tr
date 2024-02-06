# Searching

def search(request, model, model_context):
    if not request.GET:
        return {
            'data': {"message": "You have to use the GET method for this path."},
            'status': 403
        }
    
    filtered_objects = model.objects.all()
    genre = year = sorting = None
    if 'genre' in request.GET:
        filtered_objects, genre = filter(request, 'genre', filtered_objects)

    if 'year' in request.GET:
        filtered_objects, year = filter(request, 'year', filtered_objects)

    if 'sort' in request.GET:
        filtered_objects, sorting = sort(request.GET.get('sort'), filtered_objects)

    search_query = request.GET.get('search-query', None)
    search_query = search_query.strip()

    if search_query is None: 
        return {
            'data': {"message": "No search query provided."},
            'status': 400,
        }
    
    objects = filtered_objects.filter(title__icontains=search_query)
    objects |= filtered_objects.filter(keywords__icontains=search_query) # Union of two querysets

    all_genres = model.objects.values_list('genre', flat=True).distinct()
    all_years = set(map(lambda x: x.year, model.objects.values_list('date', flat=True).distinct()))

    if len(objects) == 0:  
        return {
            'data':  {"message": "No article object found.", model_context: None, "genres": all_genres, "fgenre": genre, "years": all_years, "fyear": year, "sorting": sorting, "search_query": search_query},
            'status': 404,
        }
    
    return {
        'data': {model_context: objects, "genres": all_genres, "fgenre": genre, "years": all_years, "fyear": year, "sorting": sorting, "search_query": search_query},
        'status': 200,
    }

# Filter view 

def filter(request, field, prefiltered):
    if field == "genre":
      curr_genre = request.GET.get('genre')
      return prefiltered.filter(genre=curr_genre), curr_genre
    elif field == "year":
      curr_year = request.GET.get('year')
      return prefiltered.filter(date__icontains=curr_year), curr_year
    else: 
      return prefiltered, None
    
# Sorting view 
    
def sort(field, prefiltered):
    if field == "date":
        return prefiltered.order_by('date').reverse(), field 
    elif field == "a-z":
        return prefiltered.order_by('title'), field 
    else: 
        return prefiltered, None