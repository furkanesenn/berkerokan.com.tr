from django.urls import path 

from . import views

urlpatterns = [
  path('send/<int:object_id>', views.comment_send, name='comment-send'),
  path('reply/<int:comment_id>', views.comment_reply, name='comment-reply'),
  path('<int:comment_id>/delete', views.comment_delete, name='comment-delete'),
  path('<int:comment_id>/edit', views.comment_edit, name='comment-edit'),
  path('<int:comment_id>/like', views.comment_like, name='comment-like'),
  path('<int:comment_id>/report', views.comment_report, name='comment-report'),
]