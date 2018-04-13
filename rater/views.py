from django.shortcuts import render, HttpResponse
from . import forms


def index(request):
    return render(request, 'index.html')


def rate(request):
    form = forms.RateMandarin()
    return render(request, "rate.html", {'form': form})
