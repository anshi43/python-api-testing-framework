import requests

from api.client import FakeStoreAPIClient
from test_data.carts import NEW_CART_PAYLOAD


def _cloudflare_response(url: str):
    response = requests.Response()
    response.status_code = 403
    response.url = url
    response.headers["Content-Type"] = "text/html"
    response._content = b"<!DOCTYPE html><title>Just a moment...</title>"
    return response


def test_get_products_by_category_uses_fallback_on_cloudflare_block(monkeypatch):
    api_client = FakeStoreAPIClient()

    def fake_request(method, url, **kwargs):
        return _cloudflare_response(url)

    monkeypatch.setattr("api.client.requests.request", fake_request)

    response = api_client.get_products_by_category("electronics")
    products = response.json()

    assert response.status_code == 200
    assert isinstance(products, list)
    assert len(products) > 0
    assert all(product["category"] == "electronics" for product in products)


def test_create_cart_uses_fallback_on_cloudflare_block(monkeypatch):
    api_client = FakeStoreAPIClient()

    def fake_request(method, url, **kwargs):
        return _cloudflare_response(url)

    monkeypatch.setattr("api.client.requests.request", fake_request)

    response = api_client.create_cart(NEW_CART_PAYLOAD)
    data = response.json()

    assert response.status_code == 201
    assert data["userId"] == NEW_CART_PAYLOAD["userId"]
    assert data["products"] == NEW_CART_PAYLOAD["products"]
