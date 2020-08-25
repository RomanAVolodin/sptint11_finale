from rest_framework import viewsets, filters, mixins
from rest_framework.viewsets import GenericViewSet

from .models import Category, Genre
from .serializers import CategorySerializer
from users.rbac import AnyoneCanSeeListAdminCanEdit


class CategoriesViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    serializer_class = CategorySerializer
    permission_classes = (AnyoneCanSeeListAdminCanEdit,)
    queryset = Category.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(CategoriesViewSet):
    queryset = Genre.objects.all()
