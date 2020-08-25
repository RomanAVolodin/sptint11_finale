from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Category, Genre


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
