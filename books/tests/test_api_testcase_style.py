from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from books.models import Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Atomic Habits",
            author="James Clear",
            published_year=2018,
            available=True
        )
        self.url = reverse("book-list")

    def test_get_books_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Atomic Habits")
