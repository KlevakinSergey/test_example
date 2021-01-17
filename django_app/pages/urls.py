from django.urls import path
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name='index')
]
if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
