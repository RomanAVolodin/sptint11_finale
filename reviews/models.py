from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Review(models.Model):
    text = models.TextField(verbose_name=_('Review text'))
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('Author')
    )
    score = models.PositiveIntegerField(
        verbose_name=_('Artwork rating'), validators=(MaxValueValidator(10),)
    )
    pub_date = models.DateTimeField(
        _('Date of publication'), auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
        ordering = ('-pub_date',)


class Comment(models.Model):
    text = models.TextField(verbose_name=_('Comment text'))
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('Author')
    )
    pub_date = models.DateTimeField(
        _('Date of publication'), auto_now_add=True, db_index=True
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name=_('Comments')
    )

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ('-pub_date',)
