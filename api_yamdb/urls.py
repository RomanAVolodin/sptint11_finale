from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('artworks.urls')),
    path('api/v1/', include('reviews.urls')),
    path('admin/', admin.site.urls),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc',
    ),
]
