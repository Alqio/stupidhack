from django.shortcuts import render, HttpResponse
from . import forms


# Create your views here.
def index(request):
    return HttpResponse("mandariini")


def rate(request):
    form = forms.RateMandarin()
    return render(request, "rate.html", {'form': form})
