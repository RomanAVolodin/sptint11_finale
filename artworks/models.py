import textwrap
from django.db import models
from django.db.models import Avg
from django.utils.translation import gettext_lazy as _
from slugify import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


TEXT_SHORTEN_SIMBOLS_AMOUNT = 50
MIN_YEAR = 1984


class Category(models.Model):
    name = models.CharField(
        max_length=500, verbose_name=_('Category title'), unique=True
    )
    slug = models.SlugField(
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
        if self.slug is None or self.slug == '':
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Genre(models.Model):
    name = models.CharField(
        max_length=500, verbose_name=_('Genre title'), unique=True
    )
    slug = models.SlugField(
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
        if self.slug is None or self.slug == '':
            self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)


def max_value_current_year(value):
    return MaxValueValidator(datetime.date.today().year)(value)


class Title(models.Model):
    name = models.CharField(
        max_length=500, verbose_name=_('Title'), null=False, blank=False
    )
    year = models.PositiveIntegerField(
        verbose_name=_('Year'),
        validators=[MinValueValidator(MIN_YEAR), max_value_current_year],
    )
    description = models.TextField(
        verbose_name=_('Description'), null=True, blank=True
    )
    genre = models.ManyToManyField(
        Genre, related_name='titles', verbose_name=_('Genres')
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True,
        blank=True,
        verbose_name=_('Category'),
    )

    @property
    def rating(self):
        return self.reviews.aggregate(avg=Avg('score')).get('avg')

    class Meta:
        verbose_name = _('Artwork')
        verbose_name_plural = _('Artworks')
        ordering = ('-name',)

    def __str__(self):
        return textwrap.shorten(
            self.name, width=TEXT_SHORTEN_SIMBOLS_AMOUNT, placeholder='...'
        )
