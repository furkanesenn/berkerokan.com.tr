from django.shortcuts import render, redirect, HttpResponse

from . import models
from core.utils import search_engine, interactions, session_manager

"""
TODOS:

- Utilize article/book view
- Add view and other stats to the models. 
- Add article stats view. 
- Make the URLs Turkish. 
- Embed a rich text editor for the django admin. - Done

"""

# All articles view 

def articles_list(request):
    articles = models.Article.objects.all()

    if len(articles) == 0:
        return render(request, 'articles_list.html', {"message": "No article object found.", "articles": None, "genres": None, "years": None}, status=404)
    
    all_genres = models.Article.objects.values_list('genre', flat=True).distinct() # Get all unique genres
    all_years = map(lambda x: x.year, models.Article.objects.values_list('date', flat=True).distinct()) # Get all unique years 
    # values_list: Returns a QuerySet that returns dictionaries, rather than model instances, when used as an iterable.
    # flat: If True, this will be a flat list of single values instead of a list of one-tuples.
    # distinct: Returns a new QuerySet that uses SELECT DISTINCT in its SQL query.
    articles, _ = search_engine.sort("a-z", articles)
    return render(request, 'articles_list.html', {"articles": articles, "genres": all_genres, "years": all_years}, status=200)


# Single article view

def article_detail(request, article_id: int): 
  article = models.Article.objects.get(id=article_id)
  article.view()

  if article is None: 
    all_articles = models.Article.objects.all()
    return render(request, 'articles_list.html', {'articles': all_articles, 'error': 'Article not found'}, status=404)

  return render(request, 'article_detail.html', {'article': article}, status=200)

# Search article view

def article_search(request):
    search_result = search_engine.search(request, models.Article, 'articles')
    return render(request, 'articles_list.html', search_result['data'], status=search_result['status'])

# Like article view 

@interactions.cooldown(5)
def article_like(request, article_id: int):
    session = session_manager.SessionManager(request)
    article = models.Article.objects.get(id=article_id)
    article_id = str(article_id)

    if session.has_sub_key('liked_articles', article_id):
        session.delete('liked_articles', article_id)
        article.dislike()
        return redirect('articles:article-detail', article_id=article_id)
    
    if article.like() == True:
        session.set_map_value('liked_articles', article_id, article.title)
    
    return redirect('articles:article-detail', article_id=article_id)

# Article stats view