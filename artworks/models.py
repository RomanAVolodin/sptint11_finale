import textwrap
from django.db import models
from django.utils.translation import ugettext_lazy as _
from slugify import slugify


TEXT_SHORTEN_SIMBOLS_AMOUNT = 50


class Category(models.Model):
    name = models.CharField(
        max_length=500, verbose_name=_('Category title'), unique=True
    )
    slug = models.CharField(
        max_length=500, verbose_name=_('Category slug'), unique=True
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('-name',)

    def __str__(self):
        return textwrap.shorten(
            self.name, width=TEXT_SHORTEN_SIMBOLS_AMOUNT, placeholder='...'
        )

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Genre(models.Model):
    name = models.CharField(
        max_length=500, verbose_name=_('Genre title'), unique=True
    )
    slug = models.CharField(
        max_length=500, verbose_name=_('Genre slug'), unique=True
    )

    class Meta:
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')
        ordering = ('-name',)

    def __str__(self):
        return textwrap.shorten(
            self.name, width=TEXT_SHORTEN_SIMBOLS_AMOUNT, placeholder='...'
        )

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)
