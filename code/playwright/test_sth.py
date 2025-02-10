import re
from playwright.sync_api import Page, expect

LOCATOR = 'xpath=//*/span[text() = "Search"]'
LOOK_FOR = 'xpath=//*[@id="docsearch-hits0-item-0"]/a/div/div[2]/span/mark'

def test_has_title(page: Page):
    page.goto("https://playwright.dev/python")

    expect(page).to_have_title(re.compile("|"))

def test_search_sth(page: Page):
    page.goto("https://playwright.dev/")

    expect(page.locator(LOCATOR)).to_be_visible()

    page.locator(LOCATOR).click()
    page.locator(LOCATOR).press_sequentially("Locators", delay=100)

    expect(page.locator(LOOK_FOR)).to_be_visible()
