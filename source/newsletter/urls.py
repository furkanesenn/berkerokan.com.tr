from django.urls import path 

from . import views 

urlpatterns = [
  path('', views.newsletter, name='newsletter'),
  path('subscribe', views.subscribe, name='subscribe'),
  path('verify', views.verify_subscription, name='verify'),
]