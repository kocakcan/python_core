import re
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("Before the test runs")

    # Go to the starting URL before each test
    page.goto("https://playwright.dev/")
    yield

    print("After the test runs")

def test_main_navigation(page: Page):
    # Assertions use the expect API
    expect(page).to_have_url("https://playwright.dev/")

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click on "Get started"
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of installation
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
