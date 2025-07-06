import factory
from books.models import Book


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker("sentence", nb_words=4)
    author = factory.Faker("name")
    published_year = 2020
    available = True
