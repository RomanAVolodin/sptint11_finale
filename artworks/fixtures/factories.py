import factory
from slugify import slugify

from artworks.models import Category, Genre

factory.Faker._DEFAULT_LOCALE = 'ru_RU'


class CategoriesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('bs')
    slug = factory.LazyAttribute(lambda o: slugify(o.name))


class GenresFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Faker('genre')
    slug = factory.LazyAttribute(lambda o: slugify(o.name))
