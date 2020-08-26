from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

from artworks.models import Title
from reviews.models import Review
from reviews.serializers import ReviewSerializer, CommentSerializer
from users.rbac import AnyoneCanSeeAdminModerAuthorCanEdit


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (AnyoneCanSeeAdminModerAuthorCanEdit,)

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        return (
            get_object_or_404(Title, id=title_id)
            .reviews.select_related('author')
            .all()
        )

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        if Review.objects.filter(
            title=title, author=self.request.user
        ).exists():
            raise ValidationError(_('Reviews already exists'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AnyoneCanSeeAdminModerAuthorCanEdit,)

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        return (
            get_object_or_404(Review, id=review_id, title__id=title_id)
            .comments.select_related('author')
            .all()
        )

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)
