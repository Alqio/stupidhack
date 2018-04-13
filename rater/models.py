from django.db import models


# Create your models here.
class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None,
                 max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Mandarin(models.Model):
    size = IntegerRangeField(min_value=1, max_value=5)
    round = IntegerRangeField(min_value=1, max_value=5)
    smooth = IntegerRangeField(min_value=1, max_value=5)
    soft = IntegerRangeField(min_value=1, max_value=5)
    elasticity = IntegerRangeField(min_value=1, max_value=5)
    orange = IntegerRangeField(min_value=1, max_value=5)
    smell = IntegerRangeField(min_value=1, max_value=5)
    hand_smell = IntegerRangeField(min_value=1, max_value=5)
    beautiful = IntegerRangeField(min_value=1, max_value=5)
    trump = IntegerRangeField(min_value=1, max_value=5)
    brown = IntegerRangeField(min_value=1, max_value=5)
    mold = IntegerRangeField(min_value=1, max_value=5)
    hand_feel = IntegerRangeField(min_value=1, max_value=5)
    spot_depth = IntegerRangeField(min_value=1, max_value=5)
    skin_thick_before = IntegerRangeField(min_value=1, max_value=5)
    temperature = IntegerRangeField(min_value=1, max_value=5)
    damage = IntegerRangeField(min_value=1, max_value=5)
    symmetrical = IntegerRangeField(min_value=1, max_value=5)
    plastic = IntegerRangeField(min_value=1, max_value=5)
    stem_loose = IntegerRangeField(min_value=1, max_value=5)
    opening = IntegerRangeField(min_value=1, max_value=5)
    skin_thick_after = IntegerRangeField(min_value=1, max_value=5)
    slice_size = IntegerRangeField(min_value=1, max_value=5)
    pith_amount = IntegerRangeField(min_value=1, max_value=5)
    pith_color = IntegerRangeField(min_value=1, max_value=5)
    seeds = IntegerRangeField(min_value=1, max_value=5)
    taste = IntegerRangeField(min_value=1, max_value=5)

