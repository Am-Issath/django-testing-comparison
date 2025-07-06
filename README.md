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
git clone <repo>
cd bookstore
poetry install  # or pip install -r requirements.txt
pytest
