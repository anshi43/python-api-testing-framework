def test_non_existing_product_returns_empty_body_or_non_success_payload(api_client):
    response = api_client.get_single_product(9999)

    assert response.status_code in [200, 404]

    if response.text.strip():
        data = response.json()
        assert not (isinstance(data, dict) and data.get("id") == 9999)
    else:
        assert response.text == ""


def test_non_existing_category_returns_empty_list_or_not_found(api_client):
    response = api_client.get_products_by_category("category-does-not-exist")

    assert response.status_code in [200, 404]

    if response.text.strip():
        data = response.json()
        assert data == [] or data == {}
    else:
        assert response.text == ""