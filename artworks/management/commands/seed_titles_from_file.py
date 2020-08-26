from django.core.management import BaseCommand
from django.utils.translation import ugettext_lazy as _
import csv
import os
from django.conf import settings

from artworks.models import Title, Category


class Command(BaseCommand):
    help = _('Seeds the database from file.')

    def handle(self, *args, **options):
        filename = os.path.join(
            settings.BASE_DIR, os.path.join('data', 'titles.csv')
        )
        fields = ['id', 'name', 'year', 'cat_id']
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                dictionary = dict(zip(fields, row))
                try:
                    category = Category.objects.get(id=dictionary['cat_id'])
                    del dictionary['cat_id']
                    Title.objects.create(**dictionary, category=category)
                except ValueError:
                    pass
