from django.core.mail import send_mail, send_mass_mail
from django.conf import settings

def send_verification_email(subscriber):
    """
    Sends a verification email to the subscriber
    """
    subject = subscriber.newsletter.verification_email_subject or 'berkerokan.com.tr - Bülten Üyeliğinizi Doğrulayın'
    message = f"""
    Merhaba {subscriber.first_name} {subscriber.last_name},
    
    {subscriber.newsletter.verification_email_content or 'Bültenimize hoş geldiniz. Aboneliğinizi doğrulamak için aşağıdaki linke tıklayın.'}

    http://localhost:8000/newsletter/verify?token={subscriber.subscription_token}
    """

    return send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[subscriber.email],
        fail_silently=False # Change this to True in production
    )

def send_welcome_email(subscriber):
    """
    Sends a welcome email to the subscriber
    """
    subject = subscriber.newsletter.welcome_email_subject or 'berkerokan.com.tr - Bültene Hoşgeldiniz!'
    message = f"""
    Merhaba {subscriber.first_name} {subscriber.last_name},
    
    {subscriber.newsletter.welcome_email_content or 'Bültenimize hoş geldiniz. Aboneliğiniz başarıyla aktif hale getirildi.'}
    """

    return send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[subscriber.email],
        fail_silently=False # Change this to True in production
    )

def send_custom_email(subscribers, post):
    """
    Sends a custom email to the subscriber
    """
    email_list = create_email_list(subscribers, post)
    return send_mass_mail(email_list, fail_silently=False) # Change this to True in production

def create_email_list(subscribers, post):
    """
    Creates a list of emails from the subscribers
    """
    return [[post.title, f"Merhaba {subscriber.first_name} {subscriber.last_name},\n\n{post.content}", settings.EMAIL_HOST_USER, [subscriber.email]] for subscriber in subscribers]

def retrieve_tokens(request):
    """
    Retrieves the tokens from the request session
    """
    passed_token = request.GET.get('token')
    actual_token = request.session.get('subscription_token', None)

    return passed_token, actual_token