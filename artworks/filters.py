import django_filters

from artworks.models import Title


class TitleFilter(django_filters.FilterSet):
    year = django_filters.NumberFilter()
    name = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category__slug')
    genre = django_filters.CharFilter(field_name='genre__slug')

    class Meta:
        model = Title
        fields = ('year', 'name', 'category', 'genre')
