from rest_framework import viewsets, filters

from .models import Category, Genre
from .serializers import CategorySerializer
from users.rbac import AnyoneCanSeeListAdminCanEdit


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (AnyoneCanSeeListAdminCanEdit,)
    queryset = Category.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(CategoriesViewSet):
    queryset = Genre.objects.all()
