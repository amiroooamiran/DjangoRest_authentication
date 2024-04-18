from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # Configure urls.py. Pay attention to djoser.url.authtoken module path:
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # apps urls
    path('', include('core.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
