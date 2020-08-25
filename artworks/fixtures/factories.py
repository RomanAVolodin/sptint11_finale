import factory
from slugify import slugify

from artworks.models import Category

factory.Faker._DEFAULT_LOCALE = 'ru_RU'


class CategoriesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('bs')
    slug = factory.LazyAttribute(lambda o: slugify(o.name))
