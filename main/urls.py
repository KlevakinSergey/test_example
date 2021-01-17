from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import api_root


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', api_root, name='api_root'),
    path('api/v1/accounts/', include('api.applications.accounts.urls')),
    path('pages/', include('django_app.pages.urls')),
]
if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
