from django.shortcuts import render

# Create your views here.
# Hadis

def test(request):
    return render(request, 'website/test.html')

def sevil(request):
    return render(request, 'website/sevil.html')

def about(request):
    return render(request, 'website/about.html')

def index(request):
    return render(request, 'website/index.html')

def contact(request):
    return render(request, 'website/contact.html')