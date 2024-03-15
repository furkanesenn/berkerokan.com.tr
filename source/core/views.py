from django.shortcuts import render

# Home Page / Landing View 

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, "socials.html")
