import json
from pathlib import Path
import time
import pytest
from jsonschema import validate

SCHEMAS = Path(__file__).parent / "schemas"

@pytest.mark.api
def test_get_posts_with_schema_and_latency(api, base_url):
    start = time.perf_counter()
    resp = api.get(f"{base_url}/posts")
    duration = time.perf_counter() - start

    assert resp.status_code == 200
    body = resp.json()
    schema = json.loads((SCHEMAS / "posts_list.json").read_text())
    validate(instance=body, schema=schema)

    # sanity checks
    assert isinstance(body, list) and len(body) > 0
    # latency expectation (tune if your network is slow)
    assert duration < 2.0, f"Response too slow: {duration:.2f}s"

@pytest.mark.api
def test_get_single_post_schema(api, base_url):
    resp = api.get(f"{base_url}/posts/1")
    assert resp.status_code == 200
    schema = json.loads((SCHEMAS / "post.json").read_text())
    validate(instance=resp.json(), schema=schema)
    assert resp.json()["id"] == 1

@pytest.mark.api
def test_create_post_mock(api, base_url):
    # JSONPlaceholder fakes creation and returns 201 with an id, but does not persist.
    payload = {"title": "foo", "body": "bar", "userId": 1}
    resp = api.post(f"{base_url}/posts", json=payload)
    assert resp.status_code == 201
    body = resp.json()
    # Should echo fields and include an id
    assert body.get("title") == "foo"
    assert body.get("userId") == 1
    assert "id" in body and isinstance(body["id"], int)

@pytest.mark.api
def test_unknown_route_returns_404(api, base_url):
    # Use a clearly invalid path to guarantee 404
    resp = api.get(f"{base_url}/this-route-should-not-exist-404")
    assert resp.status_code == 404
