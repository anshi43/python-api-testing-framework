import pytest
from api.client import FakeStoreAPIClient


@pytest.fixture(scope="session")
def api_client():
    return FakeStoreAPIClient()