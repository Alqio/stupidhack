from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'rate', views.rate, name='rate')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

