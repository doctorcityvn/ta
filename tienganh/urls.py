from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from hocbai import views
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView
urlpatterns = [
    path('', views.home, name='home'),
    path('nguphap/', views.nguphap, name='nguphap'),
    path('cumtu/', views.cumtu, name='cumtu'),
    path('video/', views.cumtu, name='video'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
