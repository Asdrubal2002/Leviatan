from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('users/', include('accounts.urls', namespace='users')),

    path('social/', include('social.urls', namespace='social')),

    path('marketplace/', include('marketplace.urls', namespace="marketplace")),

    path('books/', include('books.urls', namespace="books")),

    path('groups/', include('groups.urls', namespace="groups")),

    path('services/', include('services.urls', namespace="services")),

    path('', HomeView.as_view(), name="home")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
