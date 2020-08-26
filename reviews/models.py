import textwrap

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from artworks.models import Title

User = get_user_model()

TEXT_SHORTEN_SIMBOLS_AMOUNT = 50


class Review(models.Model):
    text = models.TextField(verbose_name=_('Review text'))
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Author'),
        related_name='reviews',
    )
    score = models.PositiveIntegerField(
        verbose_name=_('Artwork rating'),
        validators=(MaxValueValidator(10), MinValueValidator(1)),
    )
    pub_date = models.DateTimeField(
        _('Date of publication'), auto_now_add=True, db_index=True
    )

    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name=_('Artwork'),
        related_name='reviews',
    )

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
        ordering = ('-pub_date',)
        unique_together = ('title', 'author')

    def __str__(self):
        return textwrap.shorten(
            self.text, width=TEXT_SHORTEN_SIMBOLS_AMOUNT, placeholder='...'
        )


class Comment(models.Model):
    text = models.TextField(verbose_name=_('Comment text'))
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Author'),
        related_name='comments',
    )
    pub_date = models.DateTimeField(
        _('Date of publication'), auto_now_add=True, db_index=True
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('Review'),
    )

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ('-pub_date',)

    def __str__(self):
        return textwrap.shorten(
            self.text, width=TEXT_SHORTEN_SIMBOLS_AMOUNT, placeholder='...'
        )
