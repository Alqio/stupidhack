from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value' : self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)

class Mandarin(models.Model):
    size = MinMaxFloat(min_value=1.0, max_value=5.0)
    round = MinMaxFloat(min_value=1.0, max_value=5.0)
    smooth = MinMaxFloat(min_value=1.0, max_value=5.0)
    soft = MinMaxFloat(min_value=1.0, max_value=5.0)
    elasticity = MinMaxFloat(min_value=1.0, max_value=5.0)
    orange = MinMaxFloat(min_value=1.0, max_value=5.0)
    smell = MinMaxFloat(min_value=1.0, max_value=5.0)
    hand_smell = MinMaxFloat(min_value=1.0, max_value=5.0)
    beautiful = MinMaxFloat(min_value=1.0, max_value=5.0)
    trump = MinMaxFloat(min_value=1.0, max_value=5.0)
    brown = MinMaxFloat(min_value=1.0, max_value=5.0)
    mold = MinMaxFloat(min_value=1.0, max_value=5.0)
    hand_feel = MinMaxFloat(min_value=1.0, max_value=5.0)
    spot_depth = MinMaxFloat(min_value=1.0, max_value=5.0)
    skin_thick_before = MinMaxFloat(min_value=1.0, max_value=5.0)
    temperature = MinMaxFloat(min_value=1.0, max_value=5.0)
    damage = MinMaxFloat(min_value=1.0, max_value=5.0)
    symmetrical = MinMaxFloat(min_value=1.0, max_value=5.0)
    plastic = MinMaxFloat(min_value=1.0, max_value=5.0)
    stem_loose = MinMaxFloat(min_value=1.0, max_value=5.0)
    opening = MinMaxFloat(min_value=1.0, max_value=5.0)
    skin_thick_after = MinMaxFloat(min_value=1.0, max_value=5.0)
    slice_size = MinMaxFloat(min_value=1.0, max_value=5.0)
    pith_amount = MinMaxFloat(min_value=1.0, max_value=5.0)
    pith_color = MinMaxFloat(min_value=1.0, max_value=5.0)
    seeds = MinMaxFloat(min_value=1.0, max_value=5.0)
    taste = MinMaxFloat(min_value=1.0, max_value=5.0)

