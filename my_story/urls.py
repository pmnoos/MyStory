from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from chapters.views import register  # Import your registration view

# Redirect root URL to /chapters/
def home_redirect(request):
    return redirect('chapter_list')  # Use the correct named URL from `chapters/urls.py`


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chapters/', include('chapters.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'),
    path('', home_redirect, name='home'),  # Redirect root URL
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
