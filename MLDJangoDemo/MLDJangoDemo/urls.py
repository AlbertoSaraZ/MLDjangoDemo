"""MLDJangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from MemeDetector.views import ImageUploadView
from MemeDetector.views import MemeGallery
from MemeDetector.views import SingleMeme
from MemeDetector.views import DeleteMeme
from HomeApp.views import HomeView
from HomeApp.views import HomeCardView
from HomeApp.views import AboutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('home', HomeView.as_view(), name='home'),
    path('home/<slug>', HomeCardView.as_view(), name='home_card'),
    path('about', AboutView.as_view(), name='about'),
    path('meme-detector/', MemeGallery.as_view(), name='gallery'),
    path('meme-detector/gallery', MemeGallery.as_view(), name='gallery'),
    path('meme-detector/meme_upload', ImageUploadView.as_view(), name='meme_upload'),
    path('meme-detector/image/<int:pk>', SingleMeme.as_view(), name='single_meme'),
    path('meme-detector/image/<int:pk>/delete', DeleteMeme.as_view(), name='delete_meme')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
