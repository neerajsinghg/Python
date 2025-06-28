from playwright.sync_api import sync_playwright

from chrome_browser_launch import browser

with sync_playwright()as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Index.html")

    #css Selector - id-#, class - ., attribute - tagname[attribte="value"]
    #1. by using id