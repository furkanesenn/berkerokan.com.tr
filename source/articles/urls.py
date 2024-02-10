from django.urls import path 

from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.articles_list, name='articles-list'),
  path('s', views.article_search, name='article-search'),
  path('<int:article_id>/', views.article_detail, name='article-detail'),
  path('<int:article_id>/like', views.article_like, name='article-like'),
]