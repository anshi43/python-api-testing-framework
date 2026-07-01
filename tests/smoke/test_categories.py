def test_get_all_categories_returns_200(api_client):
    response = api_client.get_all_categories()

    assert response.status_code == 200


def test_get_all_categories_returns_non_empty_list(api_client):
    response = api_client.get_all_categories()
    categories = response.json()

    assert isinstance(categories, list)
    assert len(categories) > 0


def test_products_by_category_return_matching_category(api_client):
    response = api_client.get_products_by_category("electronics")
    products = response.json()

    assert response.status_code == 200
    assert isinstance(products, list)
    assert len(products) > 0

    for product in products:
        assert product["category"] == "electronics"