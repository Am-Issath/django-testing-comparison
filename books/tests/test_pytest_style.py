import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from books.models import Book


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_get_books_list(api_client):
    Book.objects.create(title="Deep Work", author="Cal Newport", published_year=2016, available=True)
    url = reverse("book-list")
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data[0]["title"] == "Deep Work"
