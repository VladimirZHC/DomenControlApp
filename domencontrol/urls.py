from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from . import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static





urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('control.urls')),
    path('openapi/', TemplateView.as_view(template_name="index.html")),
] + static(settings.STATIC_URL)
