from django.shortcuts import redirect

def cooldown(func, cooldown_time: int = 5):
    def wrapper(*args, **kwargs):
        request = args[0]
        if request.COOKIES.get('cooldown', False):
            return redirect(request.META.get('HTTP_REFERER', '/'))
            return
        
        response = func(*args, **kwargs)
        response.set_cookie('cooldown', True, max_age=cooldown_time, samesite='Lax')

        return response
    return wrapper