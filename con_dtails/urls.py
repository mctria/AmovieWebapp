from django.urls import path
from django.conf import settings
from .views import About, contact, privacy, term
from django.conf.urls.static import static

# Path

urlpatterns = [
    path('about/',About,name='about'),
    path('contact/',contact,name='contact'),
    path('terms-and-conditions/',term,name='term'),
    path('privacy-policy/',privacy,name='privacy_policy'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)