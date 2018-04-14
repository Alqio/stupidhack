from django import forms
from .models import Mandarin


class RateMandarin(forms.ModelForm):

    class Meta:
        model = Mandarin
        NUMBER_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        fields = '__all__'
        required = True,
        widgets = {
            'size': forms.RadioSelect(choices=NUMBER_CHOICES),
            'round': forms.RadioSelect(choices=NUMBER_CHOICES),
            'smooth': forms.RadioSelect(choices=NUMBER_CHOICES),
            'soft': forms.RadioSelect(choices=NUMBER_CHOICES),
            'elasticity': forms.RadioSelect(choices=NUMBER_CHOICES),
            'orange': forms.RadioSelect(choices=NUMBER_CHOICES),
            'smell': forms.RadioSelect(choices=NUMBER_CHOICES),
            'hand_smell': forms.RadioSelect(choices=NUMBER_CHOICES),
            'beautiful': forms.RadioSelect(choices=NUMBER_CHOICES),
            'trump': forms.RadioSelect(choices=NUMBER_CHOICES),
            'brown': forms.RadioSelect(choices=NUMBER_CHOICES),
            'mold': forms.RadioSelect(choices=NUMBER_CHOICES),
            'hand_feel': forms.RadioSelect(choices=NUMBER_CHOICES),
            'spot_depth': forms.RadioSelect(choices=NUMBER_CHOICES),
            'skin_thick_before': forms.RadioSelect(choices=NUMBER_CHOICES),
            'temperature': forms.RadioSelect(choices=NUMBER_CHOICES),
            'damage': forms.RadioSelect(choices=NUMBER_CHOICES),
            'symmetrical': forms.RadioSelect(choices=NUMBER_CHOICES),
            'plastic': forms.RadioSelect(choices=NUMBER_CHOICES),
            'stem_loose': forms.RadioSelect(choices=NUMBER_CHOICES),
            'opening': forms.RadioSelect(choices=NUMBER_CHOICES),
            'skin_thick_after': forms.RadioSelect(choices=NUMBER_CHOICES),
            'slice_size': forms.RadioSelect(choices=NUMBER_CHOICES),
            'pith_amount': forms.RadioSelect(choices=NUMBER_CHOICES),
            'pith_color': forms.RadioSelect(choices=NUMBER_CHOICES),
            'seeds': forms.RadioSelect(choices=NUMBER_CHOICES),
            'taste': forms.RadioSelect(choices=NUMBER_CHOICES)
        }