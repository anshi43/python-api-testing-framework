from test_data.carts import NEW_CART_PAYLOAD


def test_create_cart_returns_success_status(api_client):
    response = api_client.create_cart(NEW_CART_PAYLOAD)

    assert response.status_code in [200, 201]


def test_create_cart_returns_expected_payload_fields(api_client):
    response = api_client.create_cart(NEW_CART_PAYLOAD)
    data = response.json()

    assert "id" in data
    assert "userId" in data
    assert "products" in data


def test_create_cart_returns_same_user_id(api_client):
    response = api_client.create_cart(NEW_CART_PAYLOAD)
    data = response.json()

    assert data["userId"] == NEW_CART_PAYLOAD["userId"]


def test_create_cart_returns_products_list(api_client):
    response = api_client.create_cart(NEW_CART_PAYLOAD)
    data = response.json()

    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0