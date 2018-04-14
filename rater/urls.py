from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^slider/$', views.slider, name='slider'),
    url(r'rate/', views.rate, name='rate'),
    url(r'eatornot/', views.eatornot, name='eatornot')
    url(r'mymandarines/', views.my_mandarines, name='mymandarines')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


