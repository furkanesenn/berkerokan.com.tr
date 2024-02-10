from django.shortcuts import HttpResponse, redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from . import models
from articles.models import Article
from books.models import Book

from newsletter.utils import validation, email
from core.utils import session_manager, interactions

"""
TODOS:

- Make the code cleaner and more readable
- Add captcha support
- Create a session manager for the comments - Done
- Add a rate limiter - Done
- Add a spam filter - Done
- Implement mail notifications - Done
- Incorporate read only fields into admin panel and cooldown times  - Done
- Combbine two comment sending views into one generic view
"""

def only_comment_owner(func):
  def wrapper(request, comment_id, *args, **kwargs):
    session = session_manager.SessionManager(request)

    comment = models.Comment.objects.get(id=comment_id)

    if not session.has('written_comments', comment.access_token):
      return HttpResponse('Unauthorized', status=401)
    
    return func(request, comment_id, *args, **kwargs)
  return wrapper

# Send a comment view - TODO: Make the code cleaner

@interactions.cooldown(120)
def comment_send(request, object_id):

  if request.method != 'POST':
    return HttpResponse('Method not allowed', status=405)
  
  content_type_text = request.POST.get('content-type')
  content_type = ContentType.objects.get(app_label=content_type_text + 's', model=content_type_text.lower())

  object = None 
  if content_type_text == 'article':
    object = Article.objects.get(id=object_id)
  elif content_type_text == 'book':
    object = Book.objects.get(id=object_id)
  else:
    return HttpResponse('Invalid content type', status=400)

  first_name = request.POST.get('first-name')
  last_name = request.POST.get('last-name')
  email = request.POST.get('email')
  email_notification = request.POST.get('notify-me')

  # Test the validation functions
  if not validation.validate_credentials(email, first_name, last_name):
    return HttpResponse('Invalid name or email', status=400)
  
  body = request.POST.get('body')

  comment = models.Comment.objects.create(
    content_type=content_type,
    object_id=object.id,
    author=f'{first_name} {last_name}',
    author_email=email,
    body=body,
    email_notification=bool(email_notification)
  )

  session = session_manager.SessionManager(request)
  session.append('written_comments', comment.access_token)

  return redirect(reverse(f'{content_type_text}s:' + content_type_text + '-detail', args=[object_id]))

# Delete a comment view

@only_comment_owner
def comment_delete(request, comment_id):
  comment = models.Comment.objects.get(id=comment_id)

  if comment is None:
    return HttpResponse('Comment not found', status=404)

  object = comment.content_object
  comment.delete()
  return redirect(comment.content_type.model + 's:' + comment.content_type.model + '-detail', object.id)

# Edit a comment view - TODO: Compare old and new comment bodies for performance

@only_comment_owner 
def comment_edit(request, comment_id):
  comment = models.Comment.objects.get(id=comment_id)

  if comment is None:
    return HttpResponse('Comment not found', status=404)
  
  comment.body = request.GET.get('body')
  comment.save()

  return redirect(comment.content_type.model + 's:' + comment.content_type.model + '-detail', comment.object_id)

# Reply to a comment view

def comment_reply(request, comment_id):
  if request.method != 'POST':
    return HttpResponse('Method not allowed', status=405)

  comment = models.Comment.objects.get(id=comment_id)

  if comment is None:
    return HttpResponse('Comment not found', status=404)
  
  content_type = ContentType.objects.get(app_label='comments', model='comment')

  first_name = request.POST.get('first-name')
  last_name = request.POST.get('last-name')
  _email = request.POST.get('email')
  body = request.POST.get('body')
  email_notification = request.POST.get('notify-me')

  # Test the validation functions
  if not validation.validate_credentials(_email, first_name, last_name):
    return HttpResponse('Invalid name or email', status=400)

  sub_comment = models.Comment.objects.create(
    content_type = content_type,
    object_id = comment.pk,
    author = f'{first_name} {last_name}',
    author_email = _email,
    body = body,
    email_notification = bool(email_notification)
  )

  # Add the comment to the session / cookie to prevent spamming
  session = session_manager.SessionManager(request)
  session.append('written_comments', sub_comment.access_token)

  if bool(comment.email_notification):
    email.send_comment_notification(comment)

  return HttpResponse('OK')

# Like a comment view

def comment_like(request, comment_id):
  comment = models.Comment.objects.get(id=comment_id)

  if comment is None:
    return HttpResponse('Comment not found', status=404)

  session = session_manager.SessionManager(request)

  if session.has('liked_comments', comment.access_token):
    session.remove('liked_comments', comment.access_token)
    comment.dislike()
  else:
    session.append('liked_comments', comment.access_token)
    comment.like()

  return redirect(comment.content_type.model + 's:' + comment.content_type.model + '-detail', comment.object_id)

# Report a comment view

def comment_report(request, comment_id):
  comment = models.Comment.objects.get(id=comment_id)

  if comment is None:
    return HttpResponse('Comment not found', status=404)
  
  session = session_manager.SessionManager(request)

  if session.has('reported_comments', comment.access_token):
    session.remove('reported_comments', comment.access_token)
    comment.unreport()
  else:
    session.append('reported_comments', comment.access_token)
    comment.report()
  
  return redirect(comment.content_type.model + 's:' + comment.content_type.model + '-detail', comment.object_id)