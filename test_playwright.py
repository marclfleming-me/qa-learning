from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Launch Chromium browser
        browser = p.chromium.launch(headless=False)  # headless=False opens a visible window
        page = browser.new_page()

        # Navigate to example.com
        page.goto("https://example.com")

        # Print the page title
        print("Page title:", page.title())

        # Close the browser
        browser.close()

if __name__ == "__main__":
    run()