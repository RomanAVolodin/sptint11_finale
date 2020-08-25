from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoriesViewSet


router = DefaultRouter()
router.register('categories', CategoriesViewSet, basename='categories')

urlpatterns = [path('', include(router.urls))]
