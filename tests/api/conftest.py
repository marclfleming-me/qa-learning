import os
import pytest
import requests

def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default=os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com"), help="Base URL for API tests")

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("--base-url").rstrip("/")

@pytest.fixture(scope="session")
def api():
    """Provide a requests.Session configured for the API."""
    s = requests.Session()
    s.headers.update({"Accept": "application/json"})
    yield s
    s.close()
