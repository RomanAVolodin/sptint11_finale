from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Comment, Review


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fieldsets = ((_('Main info'), {'fields': ('text', 'author', 'review')}),)
    list_display = ('pk', 'author', 'pub_date')
    search_fields = ('text',)
    ordering = ('-pub_date',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('author', 'score')}),
        (_('Detail info'), {'fields': ('text',)}),
    )
    list_display = ('author', 'score', 'pub_date', 'text')
    search_fields = ('text',)
    ordering = ('-pub_date',)
