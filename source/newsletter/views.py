from django.shortcuts import render, redirect

from . import models
from newsletter.utils import email, validation

"""
TODOS:

- Models may not be exist, make a try and except block to handle the error(s)
- Add email verification - Done
- Add format values to the email and name fields - Done
- Add django forms to handle the form data
- Add post timing to the newsletter
- Fix gaps in the email content
"""

# Newsletter index view

def newsletter(request):
    latest_post = models.Post.objects.latest('published_at') # latest() returns the latest object in the database according to the field specified
    newsletter = models.Newsletter.objects.latest('created_at') # latest() returns the latest object in the database according to the field specified 

    return render(request, 'newsletter.html', {'latest_post': latest_post, 'newsletter': newsletter})

# Subscribe view

def subscribe(request):
    if request.method != 'POST':
        return redirect('newsletter')
    
    newsletter = models.Newsletter.objects.latest('created_at') 

    _email = request.POST.get('email').lower()
    first_name = request.POST.get('first-name').lower().capitalize()
    last_name = request.POST.get('last-name').lower().capitalize()

    if not validation.validate_credentials(_email, first_name, last_name):
        return render(request, 'subscription-error.html', {'error': 'Invalid credentials'}, status=400)

    subscriber: models.Subscriber = models.Subscriber.objects.create(
        email=_email, 
        first_name=first_name,
        last_name=last_name,
        newsletter=newsletter
    )

    request.session['subscription_token'] = subscriber.subscription_token

    newsletter.subscriber_count += 1
    newsletter.save()

    email.send_verification_email(subscriber)

    return render(request, 'subscribed.html', {'subscriber': subscriber}, status=201)

# Verify subscription view

def verify_subscription(request):
    if request.method != "GET":
        return redirect('newsletter')
    
    passed_token, actual_token = email.retrieve_tokens(request)

    if passed_token != actual_token:
        return render(request, 'verification-error.html', {'error': 'Invalid token'}, status=400)

    subscriber: models.Subscriber = models.Subscriber.objects.get(subscription_token=passed_token)

    subscriber.subscription_confirmed = True
    subscriber.save()

    subscriber.newsletter.confirmed_subscriber_count += 1
    subscriber.newsletter.save()

    email.send_welcome_email(subscriber)

    return render(request, 'verified.html', {'subscriber': subscriber})

# Unsubscribe view
