from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Comment, Review


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fieldsets = ((_('Main info'), {'fields': ('text', 'author', 'review')}),)
    list_display = ('pk', 'author', 'pub_date', 'text', 'review')
    search_fields = ('text',)
    ordering = ('-pub_date',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    def comments_count(self, obj):
        return obj.comments.count()

    comments_count.short_description = _('Comments count')

    fieldsets = (
        (None, {'fields': ('author', 'score')}),
        (_('Artwork'), {'fields': ('title',)}),
        (_('Detail info'), {'fields': ('text',)}),
    )
    list_display = (
        'author',
        'score',
        'pub_date',
        'text',
        'title',
        'comments_count',
    )
    search_fields = ('text',)
    ordering = ('-pub_date',)
