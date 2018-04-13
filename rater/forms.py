from django import forms
from .models import Mandarin


class RateMandarin(forms.ModelForm):

    class Meta:
        model = Mandarin
        fields = '__all__'
