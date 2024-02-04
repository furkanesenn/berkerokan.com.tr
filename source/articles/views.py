from django.shortcuts import render

from . import models

# All articles view 

def articles(request):
  all_articles = models.Article.objects.all()

  return render(request, 'articles_list.html', {'articles': all_articles})

# Single article view

# Search article view

# Filter article view

# Sort article view

# Article stats view