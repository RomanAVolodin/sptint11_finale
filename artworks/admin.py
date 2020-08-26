from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Category, Genre, Title


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = ((_('Main info'), {'fields': ('name', 'slug')}),)
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    fieldsets = ((_('Main info'), {'fields': ('name', 'slug')}),)
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('name',)


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name',)}),
        (_('Detail info'), {'fields': ('description', 'genre', 'category')}),
        (_('Important dates'), {'fields': ('year',)}),
    )
    list_display = ('name', 'year', 'category', 'rating')
    search_fields = ('name', 'description')
    ordering = ('name',)
