from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Configure urls.py. Pay attention to djoser.url.authtoken module path:
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
