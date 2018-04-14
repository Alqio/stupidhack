from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from . import forms

from .models import (Mandarin)
from mandarine.models import UserProfile


def index(request):
    return render(request, 'index.html', {'RateCount': Mandarin.objects.count()})


def slider(request):
    return render(request, 'slider.html' , {'RateCount': Mandarin.objects.count()})


def my_mandarines(request):
    user = request.user
    
    if user:
        profile = UserProfile.objects.get(user=user)
        mandarines = Mandarin.objects.filter(owner=profile)
        return render(request, 'mymandarines.html', {'mandarines':mandarines})
   
    return redirect('/') 

def rate(request):
    if request.method == 'POST':
        form = forms.RateMandarin(request.POST)


        if form.is_valid():
            form.save()


            return redirect('/eatornot')
    else:
        form = forms.RateMandarin()
    
    return render(request, "rate.html", {'form': form , 'RateCount': Mandarin.objects.count()})


def eatornot(request):
    return HttpResponse("EAT IT! or don't")


