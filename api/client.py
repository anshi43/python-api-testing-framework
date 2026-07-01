import requests


class FakeStoreAPIClient:
    BASE_URL = "https://fakestoreapi.com"

    def get_all_products(self):
        return requests.get(f"{self.BASE_URL}/products")

    def get_single_product(self, product_id: int):
        return requests.get(f"{self.BASE_URL}/products/{product_id}")

    def get_all_categories(self):
        return requests.get(f"{self.BASE_URL}/products/categories")

    def get_products_by_category(self, category_name: str):
        return requests.get(f"{self.BASE_URL}/products/category/{category_name}")

    def create_cart(self, payload: dict):
        return requests.post(f"{self.BASE_URL}/carts", json=payload)