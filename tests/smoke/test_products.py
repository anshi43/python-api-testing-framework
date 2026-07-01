from test_data.products import EXPECTED_PRODUCT_KEYS


def test_get_all_products_returns_200(api_client):
    response = api_client.get_all_products()

    assert response.status_code == 200


def test_get_all_products_returns_non_empty_list(api_client):
    response = api_client.get_all_products()
    products = response.json()

    assert isinstance(products, list)
    assert len(products) > 0


def test_product_has_expected_keys(api_client):
    response = api_client.get_all_products()
    products = response.json()
    first_product = products[0]

    assert EXPECTED_PRODUCT_KEYS.issubset(first_product.keys())


def test_get_single_product_returns_correct_product(api_client):
    response = api_client.get_single_product(1)
    product = response.json()

    assert response.status_code == 200
    assert product["id"] == 1
    assert "title" in product
    assert "price" in product