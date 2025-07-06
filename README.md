# Django Testing Styles Comparison

A small Django + DRF project demonstrating the difference between:

- ✅ Traditional `APITestCase`-based testing
- ⚡️ Modern `pytest`-based testing

## 📦 Features
- Book API with basic CRUD
- DRF Token Auth
- `factory_boy` for test data
- `pytest-cov` for coverage
- `pytest-xdist` for parallel testing

## 🧪 Test Comparison

| Feature        | APITestCase         | Pytest Style         |
|----------------|---------------------|-----------------------|
| Setup          | `setUp()` method    | `@pytest.fixture`     |
| Assertions     | `self.assertEqual`  | `assert x == y`       |
| Speed          | Slower              | ⚡️ Faster (parallel)   |
| Ecosystem      | Limited             | Huge (`pytest-*`)     |

## 🚀 Getting Started

```bash
git clone https://github.com/Am-Issath/django-testing-comparison.git
cd bookstore
poetry install  # or pip install -r requirements.txt
pytest
```

---

## 📂 GitHub Repo Suggestions

- **Name**: `django-testing-patterns`
- **Tags**: `django`, `drf`, `testing`, `pytest`, `apiclient`, `unittest`
- **Description**: Learn the difference between Django’s traditional `APITestCase` and modern `pytest` testing styles with a simple Book API.

---

## 🔥 Want Me to Generate Starter Code?

Just say the word:
> “Yes, generate full repo boilerplate with both test styles”

And I’ll generate:
- Models
- Serializers
- Views
- Routes
- Two test files: one `APITestCase`, one `pytest`
- Setup files (`pytest.ini`, `conftest.py`, `requirements.txt`)

Let’s make it a project **others will star and fork.** Ready?


