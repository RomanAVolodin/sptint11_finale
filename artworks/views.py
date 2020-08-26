from rest_framework import viewsets, filters, mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from .filters import TitleFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Genre, Title
from .serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    TitleCreateUpdateSerializer,
)
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
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = (AnyoneCanSeeListAdminCanEdit,)
    queryset = (
        Title.objects.select_related('category')
        .prefetch_related('genre')
        .all()
    )

    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return TitleCreateUpdateSerializer
        return TitleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response_serializer = TitleSerializer(instance=serializer.instance)
        return Response(
            response_serializer.data, status=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        response_serializer = TitleSerializer(instance=serializer.instance)
        return Response(response_serializer.data)
