from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Model for the users of the store.

    user = Django's own User object, used for logging in to the store and fields
    such as username.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None,
                 max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


