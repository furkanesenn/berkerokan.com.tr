from django.shortcuts import redirect

def cooldown(cooldown_time):
    def pseudo_decorator(func):
        def wrapper(*args, **kwargs):
            request = args[0]
            if request.COOKIES.get('cooldown', False):
                return redirect(request.META.get('HTTP_REFERER', '/'))
            
            response = func(*args, **kwargs)
            response.set_cookie('cooldown', True, max_age=cooldown_time, samesite='Lax')

            return response
        return wrapper
    return pseudo_decorator