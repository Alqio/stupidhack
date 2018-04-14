from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from . import forms
from mandarine.models import UserProfile
from .models import Mandarin

def index(request):
    return render(request, 'index.html')


def slider(request):
    return render(request, 'slider.html')


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
            mandarin = form.save()
            eat = is_edible(mandarin)

            return render(request, 'eatornot.hmtl', {'eat':eat})
    else:
        form = forms.RateMandarin()
    
    return render(request, "rate.html", {'form': form})


def eatornot(request):

    

    return HttpResponse("EAT IT! or don't")


def is_edible(mandarin):
    summa = []
    
    fields = list(mandarin.__dict__)[2:]

    if fields['plastic'] > 1.1 or fields['mold'] > 1.1 or fields['damage']:
        return False
    elif fields['trump'] > 3 or fields['damage'] > 2.8 or fields['seeds'] > 2.3:
        return False

    summa += sum(fields.values())
    print("summa: " + summa)
    
    if summa > 30 and summa < 45:
        return True
    else:
        return False
     
