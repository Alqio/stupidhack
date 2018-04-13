from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')

def slider(request):
    return render(request, 'slider.html')

# Create your views here.
