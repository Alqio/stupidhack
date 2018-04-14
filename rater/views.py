from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from . import forms
from .models import (Mandarin)

def index(request):
    return render(request, 'index.html', {'RateCount': Mandarin.objects.count()})

def slider(request):
    return render(request, 'slider.html')

def rate(request):
    if request.method == 'POST':
        form = forms.RateMandarin(request.POST)


        if form.is_valid():
            form.save()


            return redirect('/eatornot')
    else:
        form = forms.RateMandarin()
    
    return render(request, "rate.html", {'form': form})


def eatornot(request):
    return HttpResponse("EAT IT! or don't")


