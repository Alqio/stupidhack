from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from . import forms

from mandarine.models import UserProfile
from .models import Mandarin



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
    print("entering rate func")

    if request.method == 'POST':
        form = forms.RateMandarin(request.POST)
        print("created form") 
        if form.is_valid():
            print("form was valid")
            mandarin = form.save()
            eat = is_edible(mandarin)
            print("eat:", eat)

            return render(request, 'eatornot.html', {'eat':eat})

    else:
        form = forms.RateMandarin()
    
    return render(request, "rate.html", {'form': form , 'RateCount': Mandarin.objects.count()})


def eatornot(request):
    return render(request, "eatornot.html", {'RateCount': Mandarin.objects.count()})


def is_edible(mandarin):
    summa = []
    
    end = 0    
    print("jou") 

    field_names = [f.name for f in mandarin._meta.fields]
    fields = {}
    for field_name in field_names[3:]:
        print(field_name)
        value = getattr(mandarin, field_name, None)
        print(value)
        if field_name is not 'id' and field_name is not 'name':
            try:
                summa.append(value)
                fields.update({field_name:value})
            except:
                print("could not add field" + field_name)
        
    print(summa)
    end += sum(fields.values())
    print("summa: " , end)
    if fields['plastic'] > 1.1 or fields['mold'] > 1.1 or fields['damage']:
        return False
    elif fields['trump'] > 3 or fields['damage'] > 2.8 or fields['seeds'] > 2.3:
        return False

    
    if end > 65 and end < 84:
        return True
    else:
        return False
     

