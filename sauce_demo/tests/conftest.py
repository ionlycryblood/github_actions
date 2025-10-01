import allure
from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(params=['chromium','firefox', 'webkit'])
def page(request):
    with sync_playwright() as p:
        browser = getattr(p, request.param).launch()
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
