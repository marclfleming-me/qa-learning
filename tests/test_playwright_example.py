import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.browser
def test_example_dot_com_title():
    """Open example.com and check the title."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")
        assert page.title() == "Example Domain"
        browser.close()
